"""
Media Processor Package
This package provides utilities for processing media files.
"""

from .audio_video_utils import (
    convert_audio,
    adjust_volume,
    normalize_audio,
    merge_audio_files,
)
from .image_utils import apply_blur_filter
from .graphics_utils import add_watermark
from .pdf_utils import merge_pdfs

__all__ = [
    "convert_audio",
    "adjust_volume",
    "normalize_audio",
    "merge_audio_files",
    "apply_blur_filter",
    "add_watermark",
    "merge_pdfs",
]