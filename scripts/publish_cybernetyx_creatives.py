#!/usr/bin/env python3
"""Publish Cybernetyx pipeline creatives to GCS + Firestore."""
import base64
import json
import re
import urllib.request
from pathlib import Path

OUTLET_ID = "NLQKPp1u8Nw2SQpIBq0R"
FOLDER = Path("clients/cybernetyx/instagram/2026-08-11")
SLUGS = [
    "smart-to-intelligent-classroom-editorial",
    "bright-ai-lesson-prep-editorial",
    "teacher-hero-ai-assistant-editorial",
]
IMAGE_UPLOAD_URL = "https://image-function-926896730665.europe-west1.run.app"
FIRESTORE_URL = "https://crm-demo-2fc0c.web.app/ai-content"
API_KEY = "hexa-ai-content-666"


def post_json(url: str, payload: dict, headers: dict | None = None) -> dict:
    hdrs = {"Content-Type": "application/json", **(headers or {})}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers=hdrs,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def parse_post(path: Path) -> tuple[str, list[str]]:
    text = path.read_text()
    parts = text.split("---", 2)
    body = parts[2].strip() if len(parts) >= 3 else text
    lines = body.splitlines()
    hashtag_line_idx = None
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith("#"):
            hashtag_line_idx = i
            break
    if hashtag_line_idx is not None:
        caption = "\n".join(lines[:hashtag_line_idx]).strip()
        tags = re.findall(r"#(\w+)", lines[hashtag_line_idx])
    else:
        caption = body.strip()
        tags = []
    return caption, tags


def main():
    log_lines = [
        "# Cybernetyx — Publish Log",
        "",
        f"**Outlet ID:** `{OUTLET_ID}`",
        f"**Run date:** 2026-08-10",
        f"**Folder:** `{FOLDER}`",
        "",
    ]

    for slug in SLUGS:
        png = FOLDER / f"{slug}.png"
        post_file = FOLDER / f"{slug}-post.md"
        scores_file = FOLDER / f"{slug}-caption-scores.json"
        prompt_file = FOLDER / f"{slug}-prompt.md"

        b64 = base64.b64encode(png.read_bytes()).decode()
        upload_resp = post_json(
            IMAGE_UPLOAD_URL,
            {
                "imageUrl": f"data:image/png;base64,{b64}",
                "slug": slug,
                "prompt": (
                    "Upload this image to Firebase Storage exactly as provided. "
                    "Preserve all visible text verbatim. Aspect ratio 1:1 1080x1080."
                ),
            },
        )
        gcs_url = upload_resp.get("imageUrl")
        if not gcs_url:
            raise RuntimeError(f"GCS upload failed for {slug}: {upload_resp}")

        caption, hashtags = parse_post(post_file)
        scores = json.loads(scores_file.read_text())
        prompt = prompt_file.read_text()
        title = prompt.splitlines()[0].lstrip("# ").strip()
        excerpt = " ".join(caption.splitlines()[:2])[:200]

        fs_resp = post_json(
            FIRESTORE_URL,
            {
                "outletId": OUTLET_ID,
                "collection": "social-ai-poster",
                "slug": slug,
                "title": title,
                "caption": caption,
                "content": caption,
                "excerpt": excerpt,
                "hashtags": hashtags,
                "captionScore": scores["captionScore"],
                "captionScores": scores["captionScores"],
                "imagePrompt": prompt,
                "imageUrl": gcs_url,
                "templateName": "cybernetyx_image_post_weekly",
                "source": "brand-social-creative-pipeline",
            },
            headers={"x-api-key": API_KEY},
        )

        out_path = FOLDER / f"firestore-publish-{slug}.json"
        out_path.write_text(json.dumps(fs_resp, indent=2))

        log_lines.extend(
            [
                f"## {slug}",
                "",
                f"- **GCS imageUrl:** {gcs_url}",
                f"- **documentId:** {fs_resp.get('documentId', 'N/A')}",
                f"- **path:** {fs_resp.get('path', 'N/A')}",
                f"- **captionScore:** {scores['captionScore']}",
                f"- **status:** {'success' if fs_resp.get('documentId') or fs_resp.get('success') else 'check response'}",
                "",
            ]
        )
        print(f"Published {slug}: {fs_resp.get('documentId', fs_resp)}")

    (FOLDER / "publish-log.md").write_text("\n".join(log_lines))
    print("Done.")


if __name__ == "__main__":
    main()
