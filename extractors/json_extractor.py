"""JSON file extractor."""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)


def _flatten_json(data: Any) -> list[str]:
    """Recursively flatten JSON content into a list of string fragments."""
    fragments: list[str] = []
    if isinstance(data, dict):
        for key, value in data.items():
            fragments.append(str(key))
            fragments.extend(_flatten_json(value))
    elif isinstance(data, list):
        for item in data:
            fragments.extend(_flatten_json(item))
    else:
        fragments.append(str(data))
    return fragments


class JsonExtractor:
    """Extract text from JSON files."""

    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        """Extract text from a JSON file.

        Args:
            file_path: Path to the JSON file.

        Returns:
            Extracted text.
        """
        path = Path(file_path)
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            flattened = _flatten_json(data)
            text = " ".join(flattened)
            LOGGER.info("Extracted text from JSON: %s", path)
            return text
        except json.JSONDecodeError as exc:
            LOGGER.error("Invalid JSON in %s: %s", path, exc)
            raise
        except OSError as exc:
            LOGGER.error("Failed to read JSON %s: %s", path, exc)
            raise
