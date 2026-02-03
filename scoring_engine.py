"""Scoring engine for candidate evaluation."""
from __future__ import annotations

import logging
from dataclasses import dataclass


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class ScoreResult:
    """Structured scoring output."""

    score: float
    coverage: float
    diversity: float
    keyword_strength: float


class ScoringEngine:
    """Compute a numeric candidate score between 0 and 100."""

    @staticmethod
    def score(
        match_percentage: float,
        resume_skills: list[str],
        job_skills: list[str],
        resume_counts: dict[str, int],
        job_counts: dict[str, int],
    ) -> ScoreResult:
        """Calculate a composite score.

        Args:
            match_percentage: Match percentage value.
            resume_skills: Candidate skills list.
            job_skills: Job required skills list.
            resume_counts: Candidate skill counts.
            job_counts: Job skill counts.

        Returns:
            ScoreResult with normalized metrics and overall score.
        """
        coverage = min(max(match_percentage / 100.0, 0.0), 1.0)

        job_skill_count = max(len(job_skills), 1)
        diversity = min(len(set(resume_skills)) / job_skill_count, 1.0)

        matched_strength = sum(
            resume_counts.get(skill, 0) for skill in job_skills
        )
        total_job_strength = max(sum(job_counts.values()), 1)
        keyword_strength = min(matched_strength / total_job_strength, 1.0)

        score = (coverage * 0.6 + diversity * 0.2 + keyword_strength * 0.2) * 100
        score = max(0.0, min(score, 100.0))

        LOGGER.info(
            "Score computed: %.2f (coverage=%.2f, diversity=%.2f, strength=%.2f)",
            score,
            coverage,
            diversity,
            keyword_strength,
        )
        return ScoreResult(
            score=score,
            coverage=coverage,
            diversity=diversity,
            keyword_strength=keyword_strength,
        )
