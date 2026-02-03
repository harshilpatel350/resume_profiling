"""CLI entry point for the Resume Profiling Engine."""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from resume_profiling.extractor_router import ExtractorRouter
from resume_profiling.job_parser import JobParser
from resume_profiling.job_roles import JOB_ROLES
from resume_profiling.logger_config import configure_logging
from resume_profiling.matcher import SkillMatcher
from resume_profiling.report_generator import ReportGenerator
from resume_profiling.scoring_engine import ScoringEngine
from resume_profiling.skill_extractor import SkillExtractor
from resume_profiling.text_cleaner import TextCleaner


LOGGER = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Resume Profiling",
    )
    parser.add_argument("--resume", required=True, help="Path to resume file")
    parser.add_argument("--job", required=True, help="Path to job description file")
    parser.add_argument(
        "--output",
        default=".",
        help="Output directory for reports (default: current directory)",
    )
    parser.add_argument(
        "--log",
        default=None,
        help="Optional log file path (default: resume_profiling.log)",
    )
    return parser


def run_pipeline(resume_path: str, job_path: str, output_dir: str) -> int:
    """Run the full analysis pipeline with per-role matching.

    Args:
        resume_path: Path to resume.
        job_path: Path to job description.
        output_dir: Output directory for reports.

    Returns:
        Exit code.
    """
    try:
        resume_text_raw = ExtractorRouter.extract(resume_path)
        job_text_raw = ExtractorRouter.extract(job_path)

        resume_text = TextCleaner.clean(resume_text_raw)
        job_text = TextCleaner.clean(job_text_raw)

        resume_extractor = SkillExtractor()
        resume_result = resume_extractor.extract(resume_text)

        # Analyze per role
        role_results = []
        for role in JOB_ROLES:
            role_skill_counts = {skill: 1 for skill in role.skills}
            match_result = SkillMatcher.compare(
                resume_result.skills,
                role.skills,
                resume_result.matches,
                role_skill_counts,
            )
            score_result = ScoringEngine.score(
                match_percentage=match_result.match_percentage,
                resume_skills=resume_result.skills,
                job_skills=role.skills,
                resume_counts=resume_result.matches,
                job_counts=role_skill_counts,
            )
            role_results.append({
                "role": role.name,
                "category": role.category,
                "match_result": match_result,
                "score_result": score_result,
            })

        ReportGenerator.generate_multi_role(
            resume_skills=resume_result.skills,
            role_results=role_results,
            output_dir=output_dir,
        )
        LOGGER.info("Pipeline completed successfully")
        return 0
    except FileNotFoundError as exc:
        LOGGER.error("Missing file: %s", exc)
        return 2
    except Exception as exc:  # noqa: BLE001
        LOGGER.exception("Pipeline failed: %s", exc)
        return 1


def main() -> None:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args()

    configure_logging(log_file=args.log)
    exit_code = run_pipeline(args.resume, args.job, args.output)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
