"""TXT file extractor."""
from __future__ import annotations

import logging
from pathlib import Path


LOGGER = logging.getLogger(__name__)


class TxtExtractor:
    """Extract text from TXT files."""

    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        """Extract text from a TXT file.

        Args:
            file_path: Path to the TXT file.

        Returns:
            Extracted text.
        """
        path = Path(file_path)
        try:
            text = path.read_text(encoding="utf-8")
            LOGGER.info("Extracted text from TXT: %s", path)
            return text
        except UnicodeDecodeError:
            text = path.read_text(encoding="latin-1", errors="ignore")
            LOGGER.warning("Fallback decoding used for TXT: %s", path)
            return text
        except OSError as exc:
            LOGGER.error("Failed to read TXT %s: %s", path, exc)
            raise
