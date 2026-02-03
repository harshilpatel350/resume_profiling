"""Image OCR extractor using pytesseract and Pillow."""
from __future__ import annotations

import logging
from pathlib import Path

from PIL import Image
import pytesseract
from pytesseract import TesseractNotFoundError


LOGGER = logging.getLogger(__name__)


class ImageOCRExtractor:
    """Extract text from images using OCR."""

    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        """Extract text from an image file using OCR.

        Args:
            file_path: Path to the image file.

        Returns:
            Extracted text.
        """
        path = Path(file_path)
        try:
            with Image.open(path) as image:
                text = pytesseract.image_to_string(image)
            LOGGER.info("Extracted text from image via OCR: %s", path)
            return text
        except TesseractNotFoundError as exc:
            LOGGER.error("Tesseract OCR not found: %s", exc)
            raise
        except Exception as exc:  # noqa: BLE001
            LOGGER.error("Failed OCR extraction for %s: %s", path, exc)
            raise
