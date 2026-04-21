#!/usr/bin/env python3
"""
Higgsfield API CLI helper — Routine ortamında MCP tool yerine kullanılır.

Kullanım:
    python3 scripts/higgsfield_api.py \
        --prompt "Children's book illustration ..." \
        --output outputs/2026-04-21-sabah-9/raw/slide-1-raw.png \
        --aspect-ratio 4:5 \
        --resolution 1080p \
        --quality high \
        --reference-image-url "https://raw.githubusercontent.com/.../character-reference.png"

Gereken env değişkenleri:
    HIGGSFIELD_API_KEY
    HIGGSFIELD_API_SECRET
    (opsiyonel) HIGGSFIELD_BASE_URL — varsayılan https://platform.higgsfield.ai
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request


BASE_URL = os.environ.get("HIGGSFIELD_BASE_URL", "https://platform.higgsfield.ai").rstrip("/")
POLL_INTERVAL_S = 3
MAX_WAIT_S = 600


def log(msg: str) -> None:
    print(f"[higgsfield_api] {msg}", file=sys.stderr, flush=True)


def auth_header() -> str:
    key = os.environ.get("HIGGSFIELD_API_KEY")
    secret = os.environ.get("HIGGSFIELD_API_SECRET")
    if not key or not secret:
        log("HIGGSFIELD_API_KEY ve HIGGSFIELD_API_SECRET environment değişkenleri gerekli.")
        sys.exit(2)
    return f"Key {key}:{secret}"


def http_request(url: str, *, method: str = "POST", body: dict | None = None) -> dict:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {
        "Authorization": auth_header(),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "sincap-kitap-routine/1.0",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            text = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        err_text = e.read().decode("utf-8", errors="replace")
        log(f"HTTP {e.code} {e.reason} at {url} — {err_text}")
        raise
    return json.loads(text) if text else {}


def submit_soul_job(
    prompt: str,
    aspect_ratio: str,
    resolution: str,
    quality: str | None,
    reference_image_urls: list[str],
    seed: int | None,
) -> str:
    params: dict = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
    }
    if quality:
        params["quality"] = quality
    if reference_image_urls:
        params["reference_image_urls"] = reference_image_urls
    if seed is not None:
        params["seed"] = seed

    url = f"{BASE_URL}/v1/text2image/soul"
    log(f"POST {url}")
    resp = http_request(url, method="POST", body={"params": params})
    request_id = resp.get("request_id") or resp.get("id")
    if not request_id:
        log(f"Beklenmeyen cevap — request_id yok: {resp}")
        sys.exit(3)
    log(f"request_id = {request_id}")
    return request_id


def poll_until_done(request_id: str) -> dict:
    url = f"{BASE_URL}/requests/{request_id}/status"
    deadline = time.time() + MAX_WAIT_S
    last: dict = {}
    while time.time() < deadline:
        last = http_request(url, method="GET")
        status = last.get("status")
        log(f"status={status}")
        if status in ("completed", "failed", "nsfw", "cancelled"):
            return last
        time.sleep(POLL_INTERVAL_S)
    return last


def extract_image_url(final_response: dict) -> str:
    # Higgsfield response shapes vary; try common paths.
    candidates: list = []

    def walk(x, path=""):
        if isinstance(x, dict):
            for k, v in x.items():
                walk(v, f"{path}.{k}")
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{path}[{i}]")
        elif isinstance(x, str) and x.startswith("http") and any(
            ext in x.lower() for ext in (".png", ".jpg", ".jpeg", ".webp")
        ):
            candidates.append((path, x))

    walk(final_response)
    if not candidates:
        # Fallback — return any URL-looking string
        def walk2(x):
            if isinstance(x, dict):
                for v in x.values():
                    yield from walk2(v)
            elif isinstance(x, list):
                for v in x:
                    yield from walk2(v)
            elif isinstance(x, str) and x.startswith("http"):
                yield x
        urls = list(walk2(final_response))
        if urls:
            return urls[0]
        log(f"Final response içinde image URL bulunamadı: {final_response}")
        sys.exit(4)
    return candidates[0][1]


def download_image(url: str, output_path: pathlib.Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    log(f"İndiriliyor: {url} -> {output_path}")
    req = urllib.request.Request(url, headers={"User-Agent": "sincap-kitap-routine/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    output_path.write_bytes(data)
    log(f"Kaydedildi ({len(data)} byte)")


def main() -> None:
    p = argparse.ArgumentParser(description="Higgsfield Soul text-to-image helper")
    p.add_argument("--prompt", required=True)
    p.add_argument("--output", required=True, help="İndirilecek PNG dosya yolu")
    p.add_argument("--aspect-ratio", default="4:5")
    p.add_argument("--resolution", default="1080p")
    p.add_argument("--quality", default="high")
    p.add_argument(
        "--reference-image-url",
        action="append",
        default=[],
        help="Birden fazla --reference-image-url verilebilir",
    )
    p.add_argument("--seed", type=int)
    args = p.parse_args()

    request_id = submit_soul_job(
        prompt=args.prompt,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        quality=args.quality,
        reference_image_urls=args.reference_image_url,
        seed=args.seed,
    )
    final = poll_until_done(request_id)
    status = final.get("status")
    if status != "completed":
        log(f"İş tamamlanamadı (status={status}): {json.dumps(final)[:500]}")
        sys.exit(5)

    url = extract_image_url(final)
    download_image(url, pathlib.Path(args.output))
    # Success summary to stdout (so caller can parse if needed)
    print(json.dumps({"request_id": request_id, "image_url": url, "output": args.output}))


if __name__ == "__main__":
    main()
