"""Report generation for analysis outputs."""
from __future__ import annotations

import json
import logging
from dataclasses import asdict
from pathlib import Path
from typing import Any

from resume_profiling.matcher import MatchResult
from resume_profiling.scoring_engine import ScoreResult


LOGGER = logging.getLogger(__name__)


class ReportGenerator:
    """Generate JSON and TXT analysis reports."""

    @staticmethod
    def _build_recommendations(role_name: str, missing_skills: list[str]) -> list[str]:
        if not missing_skills:
            return [f"Strong alignment with {role_name} role. Focus on showcasing achievements."]
        recommendations = [
            f"To improve fit for {role_name}:",
            "- Address missing skills through targeted learning or certifications.",
        ]
        recommendations.append(
            f"- Prioritize learning: {', '.join(missing_skills[:5])}."
        )
        return recommendations

    @staticmethod
    def _build_fit_explanation(
        role_name: str,
        matched_skills: list[str],
        missing_skills: list[str],
        score: float,
        rank: int,
    ) -> dict[str, Any]:
        """Build detailed explanation of why a role fits the candidate."""
        
        # Categorize matched skills
        tech_skills = []
        soft_skills = []
        tools = []
        
        tech_keywords = ["python", "java", "sql", "machine learning", "deep learning", 
                        "data analysis", "statistics", "nlp", "computer vision", "aws",
                        "docker", "kubernetes", "tensorflow", "pytorch", "pandas", "numpy"]
        tool_keywords = ["tableau", "power bi", "excel", "jira", "git", "figma", 
                        "photoshop", "jenkins", "terraform", "jupyter"]
        
        for skill in matched_skills:
            skill_lower = skill.lower()
            if any(t in skill_lower for t in tool_keywords):
                tools.append(skill)
            elif any(t in skill_lower for t in tech_keywords):
                tech_skills.append(skill)
            else:
                soft_skills.append(skill)
        
        # Build fit reasons
        reasons = []
        
        if tech_skills:
            reasons.append(f"Strong technical foundation with {', '.join(tech_skills[:4])}")
        if tools:
            reasons.append(f"Proficiency in key tools: {', '.join(tools[:3])}")
        if len(matched_skills) >= 5:
            reasons.append(f"Broad skill coverage with {len(matched_skills)} matching skills")
        if score >= 50:
            reasons.append("Above-average compatibility score indicates good fit")
        elif score >= 40:
            reasons.append("Moderate compatibility with potential for growth")
        
        if not reasons:
            reasons.append(f"Shows foundational skills relevant to {role_name}")
        
        # Build growth areas
        growth_areas = []
        if missing_skills:
            critical_missing = missing_skills[:3]
            growth_areas.append(f"Key skills to develop: {', '.join(critical_missing)}")
            if len(missing_skills) > 5:
                growth_areas.append(f"{len(missing_skills) - 3} additional skills would strengthen your profile")
        
        # Build action items
        action_items = []
        if "docker" in [s.lower() for s in missing_skills]:
            action_items.append("Learn containerization with Docker for modern deployment workflows")
        if "kubernetes" in [s.lower() for s in missing_skills]:
            action_items.append("Explore Kubernetes for container orchestration")
        if any(cloud in [s.lower() for s in missing_skills] for cloud in ["aws", "azure", "gcp"]):
            action_items.append("Get certified in cloud platforms (AWS/Azure/GCP)")
        if "git" in [s.lower() for s in missing_skills]:
            action_items.append("Master Git for version control best practices")
        if any(ml in [s.lower() for s in missing_skills] for ml in ["tensorflow", "pytorch", "deep learning"]):
            action_items.append("Deepen ML/DL expertise with TensorFlow or PyTorch projects")
        
        if not action_items:
            action_items.append(f"Focus on mastering: {', '.join(missing_skills[:2])}" if missing_skills else "Continue building expertise in current skills")
        
        return {
            "rank": rank,
            "role": role_name,
            "score": score,
            "fit_summary": f"#{rank} Best Fit - {score}% match with {len(matched_skills)} skills aligned",
            "why_it_fits": reasons,
            "matched_skills": matched_skills,
            "growth_areas": growth_areas,
            "action_items": action_items[:3],
        }

    @classmethod
    def generate_multi_role(
        cls,
        resume_skills: list[str],
        role_results: list[dict[str, Any]],
        output_dir: str | Path = ".",
    ) -> dict[str, Any]:
        """Generate JSON and TXT reports with per-role analysis.

        Args:
            resume_skills: Skills extracted from resume.
            role_results: List of role analysis results.
            output_dir: Output directory for reports.

        Returns:
            Dictionary with report data.
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Sort by score descending
        sorted_results = sorted(
            role_results,
            key=lambda x: x["score_result"].score,
            reverse=True,
        )

        roles_data = []
        for res in sorted_results:
            match_result: MatchResult = res["match_result"]
            score_result: ScoreResult = res["score_result"]
            role_name = res["role"]
            category = res.get("category", "Other")
            roles_data.append({
                "role": role_name,
                "category": category,
                "match_percentage": round(match_result.match_percentage, 2),
                "score": round(score_result.score, 2),
                "matched_skills": match_result.strength_skills,
                "missing_skills": match_result.missing_skills,
                "recommendations": cls._build_recommendations(role_name, match_result.missing_skills),
            })

        best_role = sorted_results[0]["role"] if sorted_results else "N/A"
        best_score = round(sorted_results[0]["score_result"].score, 2) if sorted_results else 0

        # Build detailed explanations for TOP 3 roles
        top_3_explanations = []
        for idx, res in enumerate(sorted_results[:3]):
            match_result: MatchResult = res["match_result"]
            score_result: ScoreResult = res["score_result"]
            role_name = res["role"]
            explanation = cls._build_fit_explanation(
                role_name=role_name,
                matched_skills=match_result.strength_skills,
                missing_skills=match_result.missing_skills,
                score=round(score_result.score, 2),
                rank=idx + 1,
            )
            top_3_explanations.append(explanation)

        report_data: dict[str, Any] = {
            "candidate_skills": resume_skills,
            "best_fit_role": best_role,
            "best_fit_score": best_score,
            "top_3_job_fits": top_3_explanations,
            "roles": roles_data,
        }

        json_path = output_path / "analysis_report.json"
        txt_path = output_path / "analysis_report.txt"

        json_path.write_text(json.dumps(report_data, indent=2), encoding="utf-8")
        txt_path.write_text(cls._format_multi_role_txt(report_data), encoding="utf-8")

        LOGGER.info("Reports generated at %s", output_path)
        return report_data

    @staticmethod
    def _format_multi_role_txt(report_data: dict[str, Any]) -> str:
        lines = [
            "=" * 70,
            "                    RESUME PROFILING REPORT",
            "=" * 70,
            "",
            f"Candidate Skills Found: {len(report_data['candidate_skills'])}",
            f"Skills: {', '.join(report_data['candidate_skills'][:20])}{'...' if len(report_data['candidate_skills']) > 20 else ''}",
            "",
            "-" * 70,
            f"🏆 BEST FIT: {report_data['best_fit_role']} ({report_data['best_fit_score']}%)",
            "-" * 70,
            "",
        ]

        # =========== TOP 3 JOB FITS WITH DETAILED EXPLANATIONS ===========
        lines.append("=" * 70)
        lines.append("              🎯 TOP 3 RECOMMENDED JOB ROLES")
        lines.append("=" * 70)
        
        for fit in report_data.get("top_3_job_fits", []):
            rank = fit["rank"]
            role = fit["role"]
            score = fit["score"]
            
            # Header for each role
            medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉"
            lines.append("")
            lines.append(f"{'─' * 70}")
            lines.append(f"{medal} #{rank} - {role.upper()}")
            lines.append(f"{'─' * 70}")
            lines.append(f"   Match Score: {score}%")
            score_bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
            lines.append(f"   [{score_bar}]")
            lines.append("")
            
            # Why it fits
            lines.append("   📌 WHY THIS ROLE FITS YOU:")
            for reason in fit.get("why_it_fits", []):
                lines.append(f"      ✓ {reason}")
            lines.append("")
            
            # Matched skills
            matched = fit.get("matched_skills", [])
            lines.append(f"   ✅ MATCHING SKILLS ({len(matched)}):")
            if matched:
                # Display in rows of 4
                for i in range(0, len(matched), 4):
                    skill_row = matched[i:i+4]
                    lines.append(f"      • {', '.join(skill_row)}")
            else:
                lines.append("      None")
            lines.append("")
            
            # Growth areas
            growth = fit.get("growth_areas", [])
            if growth:
                lines.append("   📈 AREAS FOR GROWTH:")
                for area in growth:
                    lines.append(f"      ⚠ {area}")
                lines.append("")
            
            # Action items
            actions = fit.get("action_items", [])
            if actions:
                lines.append("   🚀 RECOMMENDED ACTIONS:")
                for idx, action in enumerate(actions, 1):
                    lines.append(f"      {idx}. {action}")
            
            lines.append("")

        # =========== POSITION-WISE ANALYSIS ===========
        lines.append("")
        lines.append("=" * 70)
        lines.append("              📊 ALL POSITIONS ANALYSIS (Top 15)")
        lines.append("=" * 70)

        # Group by category
        roles_by_category: dict[str, list] = {}
        for role in report_data["roles"][:15]:  # Top 15 roles
            category = role.get("category", "Other")
            if category not in roles_by_category:
                roles_by_category[category] = []
            roles_by_category[category].append(role)

        for category, roles in roles_by_category.items():
            lines.append(f"\n{'─' * 70}")
            lines.append(f"📂 {category.upper()}")
            lines.append(f"{'─' * 70}")
            
            for role in roles:
                score_bar = "█" * int(role['score'] / 10) + "░" * (10 - int(role['score'] / 10))
                lines.append(f"\n  📌 {role['role']}")
                lines.append(f"     [{score_bar}] {role['score']}%")
                lines.append(f"     ✅ Matched: {', '.join(role['matched_skills'][:8]) or 'None'}{'...' if len(role['matched_skills']) > 8 else ''}")
                lines.append(f"     ❌ Missing: {', '.join(role['missing_skills'][:5]) or 'None'}{'...' if len(role['missing_skills']) > 5 else ''}")

        lines.append(f"\n{'=' * 70}")
        lines.append("📋 RECOMMENDATIONS FOR BEST FIT ROLE:")
        lines.append("")
        best_role_data = report_data["roles"][0] if report_data["roles"] else None
        if best_role_data:
            for rec in best_role_data["recommendations"]:
                lines.append(f"  → {rec}")

        lines.append("")
        lines.append(f"{'=' * 70}")
        lines.append(f"Total Roles Analyzed: {len(report_data['roles'])}")
        lines.append(f"{'=' * 70}")
        return "\n".join(lines)

    @classmethod
    def generate(
        cls,
        match_result: MatchResult,
        score_result: ScoreResult,
        output_dir: str | Path = ".",
    ) -> dict[str, Any]:
        """Generate JSON and TXT reports (legacy single-role).

        Args:
            match_result: MatchResult data.
            score_result: ScoreResult data.
            output_dir: Output directory for reports.

        Returns:
            Dictionary with report data.
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        report_data: dict[str, Any] = {
            "match_percentage": round(match_result.match_percentage, 2),
            "cosine_similarity": round(match_result.cosine_similarity, 3),
            "missing_skills": match_result.missing_skills,
            "strength_skills": match_result.strength_skills,
            "score": round(score_result.score, 2),
            "metrics": asdict(score_result),
            "recommendations": cls._build_recommendations("this role", match_result.missing_skills),
        }

        json_path = output_path / "analysis_report.json"
        txt_path = output_path / "analysis_report.txt"

        json_path.write_text(json.dumps(report_data, indent=2), encoding="utf-8")
        txt_path.write_text(cls._format_txt(report_data), encoding="utf-8")

        LOGGER.info("Reports generated at %s", output_path)
        return report_data

    @staticmethod
    def _format_txt(report_data: dict[str, Any]) -> str:
        lines = [
            "Resume Profiling Report",
            "=" * 50,
            f"Match Percentage: {report_data['match_percentage']}%",
            f"Cosine Similarity: {report_data['cosine_similarity']}",
            f"Score: {report_data['score']}",
            "",
            "Strength Skills:",
            ", ".join(report_data["strength_skills"]) or "None",
            "",
            "Missing Skills:",
            ", ".join(report_data["missing_skills"]) or "None",
            "",
            "Recommendations:",
        ]
        for rec in report_data["recommendations"]:
            lines.append(f"- {rec}")
        return "\n".join(lines)
