"""Text normalization utilities."""
from __future__ import annotations

import regex as re


class TextCleaner:
    """Clean and normalize extracted text."""

    NON_PRINTABLE_PATTERN = re.compile(r"[\x00-\x1f\x7f-\x9f]")
    SPECIAL_CHAR_PATTERN = re.compile(r"[^a-zA-Z0-9\s\+\#\.\-/]")
    WHITESPACE_PATTERN = re.compile(r"\s+")

    @classmethod
    def clean(cls, text: str) -> str:
        """Clean extracted text.

        Steps:
            - Remove non-printable characters
            - Remove special characters
            - Lowercase
            - Normalize whitespace

        Args:
            text: Raw extracted text.

        Returns:
            Cleaned text.
        """
        text = cls.NON_PRINTABLE_PATTERN.sub(" ", text)
        text = cls.SPECIAL_CHAR_PATTERN.sub(" ", text)
        text = text.lower()
        text = cls.WHITESPACE_PATTERN.sub(" ", text).strip()
        return text
