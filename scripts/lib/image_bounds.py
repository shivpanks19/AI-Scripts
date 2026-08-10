"""Image bounds utilities — visible (non-transparent) bounding box detection."""

from __future__ import annotations

from typing import Tuple

from PIL import Image


BBox = Tuple[int, int, int, int]


def get_visible_bbox(image: Image.Image, alpha_threshold: int = 8) -> BBox:
    """Return bounding box (left, top, right, bottom) of visible pixels.

    For RGBA images, ignores pixels with alpha below threshold.
    For RGB images, uses full image bounds.
  """
    if image.mode != "RGBA":
        rgba = image.convert("RGBA")
    else:
        rgba = image

    alpha = rgba.getchannel("A")
    mask = alpha.point(lambda p: 255 if p > alpha_threshold else 0)
    bbox = mask.getbbox()
    if bbox is None:
        return (0, 0, rgba.width, rgba.height)
    return bbox


def crop_to_visible(image: Image.Image, alpha_threshold: int = 8) -> Image.Image:
    """Return a copy cropped to visible content without modifying the source file."""
    bbox = get_visible_bbox(image, alpha_threshold=alpha_threshold)
    return image.crop(bbox)


def visible_size(image: Image.Image, alpha_threshold: int = 8) -> tuple[int, int]:
    bbox = get_visible_bbox(image, alpha_threshold=alpha_threshold)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]
