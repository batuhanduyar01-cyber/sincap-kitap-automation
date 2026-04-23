#!/usr/bin/env python3
"""
Routine -> Vercel relay -> Higgsfield orchestrator.

Higgsfield'ın Cloudflare WAF'ı Anthropic Routine runner IP'lerini blokluyor
(host_not_allowed / 403). Bunun yerine Routine, bu scripti çağırır; script
Vercel üzerindeki relay'e (DNS açık olan bir ortam) istek atar; relay
Higgsfield'a submit eder ve webhook ile dönüş yapar. Üretilen PNG'ler
GitHub'a `assets/gorseller/<slot>/slide-<idx>.png` yoluna commit'lenir.

Kullanım (routine prompt içinden):

    python3 scripts/relay_api.py submit-batch \\
        --slot    2026-04-22-sabah-9 \\
        --branch  claude/2026-04-22-sabah-9 \\
        --prompts-file /tmp/prompts.json

    # prompts.json örnek:
    # [
    #   {"prompt": "...", "width_and_height": "1152x1536", "quality": "1080p"},
    #   {"prompt": "...", "width_and_height": "1152x1536", "quality": "1080p"},
    #   ...
    # ]

Zorunlu env değişkenleri:
    RELAY_URL             (örn. https://vercel-hf-probe.vercel.app)
    RELAY_SHARED_SECRET

Opsiyonel:
    RELAY_POLL_INTERVAL_S (default 10)
    RELAY_MAX_WAIT_S      (default 900 — 15 dk)

Exit kodları:
    0  başarılı (tüm slide'lar GitHub'a commit'lendi)
    2  env eksik / argüman hatası
    3  submit başarısız
    4  timeout (tüm slide'lar gelmedi)
    5  webhook tarafında hata (slide-N.error.json dosyası oluştu)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


def log(msg: str) -> None:
    print(f"[relay_api] {msg}", file=sys.stderr, flush=True)


def env_required(name: str) -> str:
    v = os.environ.get(name)
    if not v:
        log(f"HATA: {name} environment değişkeni gerekli.")
        sys.exit(2)
    return v


def relay_request(
    method: str,
    path: str,
    *,
    body: dict | None = None,
    query: dict | None = None,
) -> tuple[int, dict]:
    base = env_required("RELAY_URL").rstrip("/")
    secret = env_required("RELAY_SHARED_SECRET")

    url = base + path
    if query:
        url += "?" + urllib.parse.urlencode(query)

    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {
        "Authorization": f"Bearer {secret}",
        "Accept": "application/json",
        "User-Agent": "sincap-kitap-routine/1.0",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            text = resp.read().decode("utf-8")
            status = resp.status
    except urllib.error.HTTPError as e:
        text = e.read().decode("utf-8", errors="replace")
        status = e.code

    parsed: dict
    try:
        parsed = json.loads(text) if text else {}
    except json.JSONDecodeError:
        parsed = {"_raw": text}
    return status, parsed


def cmd_submit_batch(args: argparse.Namespace) -> int:
    with open(args.prompts_file, "r", encoding="utf-8") as f:
        prompts = json.load(f)
    if not isinstance(prompts, list) or not prompts:
        log(f"prompts-file geçersiz (boş veya liste değil): {args.prompts_file}")
        return 2

    # Normalize entries: either {"prompt": "..."} or a raw string.
    normalized = []
    for i, p in enumerate(prompts):
        if isinstance(p, str):
            normalized.append({"prompt": p})
        elif isinstance(p, dict) and "prompt" in p:
            normalized.append(p)
        else:
            log(f"prompts[{i}] geçersiz: {p!r}")
            return 2

    log(f"Submitting {len(normalized)} prompt to relay (slot={args.slot}, branch={args.branch})")
    status, resp = relay_request(
        "POST",
        "/api/hf/submit",
        body={"slot": args.slot, "branch": args.branch, "prompts": normalized},
    )
    log(f"submit HTTP {status}: {json.dumps(resp)[:800]}")
    if status >= 400:
        return 3

    subs = resp.get("submissions") or []
    any_failed_submit = any(not s.get("ok") for s in subs)
    if any_failed_submit:
        for s in subs:
            if not s.get("ok"):
                log(f"  slide-{s.get('idx')} submit FAILED: {s.get('error')} deny={s.get('deny_reason')}")
        return 3

    # Poll until status.done or timeout.
    interval = int(os.environ.get("RELAY_POLL_INTERVAL_S", "10"))
    max_wait = int(os.environ.get("RELAY_MAX_WAIT_S", "900"))
    deadline = time.time() + max_wait
    count = len(normalized)

    while time.time() < deadline:
        s_code, s_resp = relay_request(
            "GET",
            "/api/hf/status",
            query={"slot": args.slot, "branch": args.branch, "count": str(count)},
        )
        if s_code >= 400:
            log(f"status poll HTTP {s_code}: {json.dumps(s_resp)[:400]}")
            time.sleep(interval)
            continue

        found = len(s_resp.get("found") or [])
        missing = len(s_resp.get("missing") or [])
        errors = s_resp.get("errors") or []
        log(f"poll: {found}/{count} hazır, {missing} bekleniyor, errors={len(errors)}")

        if errors:
            # Any webhook-side permanent failure -> abort, surface to routine.
            log(f"Webhook hatası: {errors}")
            return 5

        if s_resp.get("done"):
            log("Tüm görseller commit'lendi.")
            # Emit a compact summary to stdout for the calling routine.
            print(json.dumps({
                "ok": True,
                "slot": args.slot,
                "branch": args.branch,
                "count": count,
                "found": s_resp.get("found") or [],
            }))
            return 0

        time.sleep(interval)

    log(f"Timeout: {max_wait}s içinde tüm görseller gelmedi.")
    return 4


def cmd_status(args: argparse.Namespace) -> int:
    s_code, s_resp = relay_request(
        "GET",
        "/api/hf/status",
        query={"slot": args.slot, "branch": args.branch, "count": str(args.count)},
    )
    print(json.dumps(s_resp, indent=2, ensure_ascii=False))
    return 0 if s_code < 400 else 1


def main() -> None:
    p = argparse.ArgumentParser(description="Vercel HF relay client")
    sub = p.add_subparsers(dest="cmd", required=True)

    sb = sub.add_parser("submit-batch", help="Bir batch prompt'u submit et ve poll et")
    sb.add_argument("--slot", required=True)
    sb.add_argument("--branch", required=True)
    sb.add_argument("--prompts-file", required=True)
    sb.set_defaults(func=cmd_submit_batch)

    st = sub.add_parser("status", help="Mevcut slot'un durumunu sorgula")
    st.add_argument("--slot", required=True)
    st.add_argument("--branch", required=True)
    st.add_argument("--count", type=int, default=5)
    st.set_defaults(func=cmd_status)

    args = p.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
