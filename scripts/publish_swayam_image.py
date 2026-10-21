#!/usr/bin/env python3
"""Generate Swayam poster locally, then upload via image-function.

Local render guarantees on-poster copy. image-function is upload/storage only —
pass the locally rendered PNG URL, never a template thumbnail with baked text.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

IMAGE_FUNCTION_URL = "https://image-function-926896730665.europe-west1.run.app"
DEFAULT_RAW_BASE = (
    "https://raw.githubusercontent.com/shivpanks19/AI-Scripts/"
    "cursor/swayam-weekly-content-pipeline-bfd3/docs/assets/swayam"
)


def run_generate(args: argparse.Namespace, out: Path) -> None:
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "generate_swayam_image.py"),
        "--headline",
        args.headline,
        "--subline",
        args.subline,
        "--stat",
        args.stat,
        "--cta",
        args.cta,
        "--slug",
        args.slug,
        "--out",
        str(out),
    ]
    subprocess.run(cmd, check=True)


def post_image_function(image_url: str, slug: str) -> dict:
    payload = {
        "imageUrl": image_url,
        "slug": slug,
        "prompt": (
            "Upload this image to Firebase Storage exactly as provided. "
            "Preserve all visible text verbatim. Do not replace headline, stat, "
            "subline, or CTA. Minor compression only. Aspect ratio 1:1 1080x1080."
        ),
    }
    req = urllib.request.Request(
        IMAGE_FUNCTION_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate + publish Swayam weekly poster.")
    parser.add_argument("--headline", required=True)
    parser.add_argument("--subline", required=True)
    parser.add_argument("--stat", required=True)
    parser.add_argument("--cta", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--raw-base",
        default=DEFAULT_RAW_BASE,
        help="Public raw GitHub base URL for docs/assets/swayam (after git push)",
    )
    parser.add_argument(
        "--skip-upload",
        action="store_true",
        help="Only generate local PNG; do not call image-function",
    )
    args = parser.parse_args()

    out = Path(f"docs/assets/swayam/{args.slug}.png")
    run_generate(args, out)
    print(f"local={out.resolve()}")

    if args.skip_upload:
        return

    public_url = f"{args.raw_base.rstrip('/')}/{args.slug}.png"
    print(f"public_source={public_url}")
    print(
        "NOTE: Push docs/assets/swayam/{slug}.png to the branch behind --raw-base "
        "before upload, or pass a different reachable --raw-base URL.",
        file=sys.stderr,
    )

    try:
        result = post_image_function(public_url, args.slug)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()
        raise SystemExit(f"image-function failed ({exc.code}): {body}") from exc

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
