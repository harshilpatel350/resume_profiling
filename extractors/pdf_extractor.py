"""PDF file extractor using PyPDF2."""
from __future__ import annotations

import logging
from pathlib import Path

from PyPDF2 import PdfReader


LOGGER = logging.getLogger(__name__)


class PdfExtractor:
    """Extract text from PDF files."""

    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        """Extract text from a PDF file.

        Args:
            file_path: Path to the PDF file.

        Returns:
            Extracted text.
        """
        path = Path(file_path)
        try:
            reader = PdfReader(str(path))
            text_parts: list[str] = []
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text_parts.append(page_text)
            text = "\n".join(text_parts)
            LOGGER.info("Extracted text from PDF: %s", path)
            return text
        except Exception as exc:  # noqa: BLE001
            LOGGER.error("Failed to extract PDF %s: %s", path, exc)
            raise
