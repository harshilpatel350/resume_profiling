"""Job description parsing and skill extraction."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Iterable

from resume_profiling.skill_extractor import SkillExtractor, SkillExtractionResult, SKILL_DICTIONARY


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class JobSkillResult:
    """Structured job skill extraction output."""

    skills: list[str]
    matches: dict[str, int]


class JobParser:
    """Extract required skills from job description text."""

    def __init__(self, skill_dictionary: Iterable[str] | None = None) -> None:
        self._extractor = SkillExtractor(skill_dictionary or SKILL_DICTIONARY)

    def extract_required_skills(self, text: str) -> JobSkillResult:
        """Extract skills from job description text.

        Args:
            text: Cleaned job description text.

        Returns:
            JobSkillResult with unique skills and counts.
        """
        result: SkillExtractionResult = self._extractor.extract(text)
        LOGGER.info("Extracted %d job skills", len(result.skills))
        return JobSkillResult(skills=result.skills, matches=result.matches)
