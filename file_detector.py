"""File type detection utilities."""
from __future__ import annotations

import logging
from pathlib import Path


LOGGER = logging.getLogger(__name__)


class UnsupportedFileTypeError(ValueError):
    """Raised when a file type is not supported."""


class FileDetector:
    """Detect supported file types based on file extension."""

    SUPPORTED_EXTENSIONS = {
        ".txt": "txt",
        ".pdf": "pdf",
        ".docx": "docx",
        ".json": "json",
        ".png": "image",
        ".jpg": "image",
        ".jpeg": "image",
    }

    @classmethod
    def detect(cls, file_path: str | Path) -> str:
        """Detect the file type for the given path.

        Args:
            file_path: Path to the file.

        Returns:
            A string representing the detected file type.

        Raises:
            FileNotFoundError: If the file does not exist.
            UnsupportedFileTypeError: If the file type is unsupported.
        """
        path = Path(file_path)
        if not path.exists():
            LOGGER.error("File not found: %s", path)
            raise FileNotFoundError(f"File not found: {path}")

        ext = path.suffix.lower()
        file_type = cls.SUPPORTED_EXTENSIONS.get(ext)
        if not file_type:
            LOGGER.error("Unsupported file type: %s", ext)
            raise UnsupportedFileTypeError(f"Unsupported file type: {ext}")

        LOGGER.info("Detected file type '%s' for %s", file_type, path)
        return file_type
