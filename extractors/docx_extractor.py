"""DOCX file extractor using python-docx."""
from __future__ import annotations

import logging
from pathlib import Path

from docx import Document


LOGGER = logging.getLogger(__name__)


class DocxExtractor:
    """Extract text from DOCX files."""

    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        """Extract text from a DOCX file.

        Args:
            file_path: Path to the DOCX file.

        Returns:
            Extracted text.
        """
        path = Path(file_path)
        try:
            document = Document(str(path))
            text_parts = [paragraph.text for paragraph in document.paragraphs]
            text = "\n".join(text_parts)
            LOGGER.info("Extracted text from DOCX: %s", path)
            return text
        except Exception as exc:  # noqa: BLE001
            LOGGER.error("Failed to extract DOCX %s: %s", path, exc)
            raise
