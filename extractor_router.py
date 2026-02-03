"""Extractor router to select appropriate extractor based on file type."""
from __future__ import annotations

import logging
from pathlib import Path

from resume_profiling.file_detector import FileDetector
from resume_profiling.extractors.docx_extractor import DocxExtractor
from resume_profiling.extractors.image_ocr_extractor import ImageOCRExtractor
from resume_profiling.extractors.json_extractor import JsonExtractor
from resume_profiling.extractors.pdf_extractor import PdfExtractor
from resume_profiling.extractors.txt_extractor import TxtExtractor


LOGGER = logging.getLogger(__name__)


class ExtractorRouter:
    """Route files to the correct extractor implementation."""

    EXTRACTOR_MAP = {
        "txt": TxtExtractor,
        "pdf": PdfExtractor,
        "docx": DocxExtractor,
        "json": JsonExtractor,
        "image": ImageOCRExtractor,
    }

    @classmethod
    def extract(cls, file_path: str | Path) -> str:
        """Extract text from a file by routing to the correct extractor.

        Args:
            file_path: Path to the file.

        Returns:
            Extracted text.
        """
        file_type = FileDetector.detect(file_path)
        extractor_cls = cls.EXTRACTOR_MAP[file_type]
        LOGGER.info("Routing %s to %s", file_path, extractor_cls.__name__)
        return extractor_cls.extract_text(file_path)
