"""Skill matching engine."""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class MatchResult:
    """Structured skill matching output."""

    match_percentage: float
    cosine_similarity: float
    missing_skills: list[str]
    strength_skills: list[str]


class SkillMatcher:
    """Compare candidate skills with job skills."""

    @staticmethod
    def _cosine_similarity(
        resume_counts: dict[str, int], job_counts: dict[str, int]
    ) -> float:
        universe = set(resume_counts) | set(job_counts)
        if not universe:
            return 0.0
        dot_product = 0.0
        resume_norm = 0.0
        job_norm = 0.0
        for skill in universe:
            resume_val = float(resume_counts.get(skill, 0))
            job_val = float(job_counts.get(skill, 0))
            dot_product += resume_val * job_val
            resume_norm += resume_val ** 2
            job_norm += job_val ** 2
        if resume_norm == 0.0 or job_norm == 0.0:
            return 0.0
        return dot_product / (math.sqrt(resume_norm) * math.sqrt(job_norm))

    @classmethod
    def compare(
        cls,
        resume_skills: list[str],
        job_skills: list[str],
        resume_counts: dict[str, int],
        job_counts: dict[str, int],
    ) -> MatchResult:
        """Compare candidate skills with job skills.

        Args:
            resume_skills: Candidate skills list.
            job_skills: Job required skills list.
            resume_counts: Candidate skill counts.
            job_counts: Job skill counts.

        Returns:
            MatchResult with match metrics.
        """
        resume_set = set(resume_skills)
        job_set = set(job_skills)

        intersection = sorted(resume_set & job_set)
        missing = sorted(job_set - resume_set)
        overlap_ratio = len(intersection) / len(job_set) if job_set else 0.0

        cosine_sim = cls._cosine_similarity(resume_counts, job_counts)
        match_percentage = overlap_ratio * 100.0

        LOGGER.info(
            "Match percentage: %.2f, cosine similarity: %.3f",
            match_percentage,
            cosine_sim,
        )

        return MatchResult(
            match_percentage=match_percentage,
            cosine_similarity=cosine_sim,
            missing_skills=missing,
            strength_skills=intersection,
        )
