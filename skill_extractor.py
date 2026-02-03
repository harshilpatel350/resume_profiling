"""Resume skill extraction logic."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Iterable

import regex as re


LOGGER = logging.getLogger(__name__)


SKILL_DICTIONARY = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "c",
    "go", "golang", "rust", "ruby", "php", "swift", "kotlin", "scala",
    "r", "matlab", "perl", "bash", "powershell", "objective-c",
    "solidity", "abap", "apex", "vba",
    
    # Web Development
    "html", "css", "sass", "react", "angular", "vue", "node.js",
    "django", "flask", "fastapi", "spring", "spring boot", ".net",
    "asp.net", "laravel", "symfony", "ruby on rails", "express",
    "next.js", "nuxt", "gatsby", "webpack", "npm", "yarn",
    
    # Mobile Development
    "ios", "android", "react native", "flutter", "swift", "kotlin",
    "xcode", "android studio", "mobile development", "app store",
    "google play", "cocoapods", "gradle",
    
    # Databases
    "sql", "mysql", "postgresql", "sqlite", "mongodb", "redis",
    "elasticsearch", "cassandra", "dynamodb", "oracle", "sql server",
    "bigquery", "redshift", "snowflake", "neo4j", "couchbase",
    "firebase", "mariadb", "nosql",
    
    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
    "terraform", "ansible", "jenkins", "gitlab", "github actions",
    "ci/cd", "linux", "windows server", "vmware", "cloudformation",
    "arm templates", "helm", "argocd", "gitops", "prometheus",
    "grafana", "datadog", "splunk", "elk", "nginx", "apache",
    
    # Data & Analytics
    "pandas", "numpy", "matplotlib", "seaborn", "tableau", "power bi",
    "looker", "qlik", "data analysis", "data visualization",
    "data cleaning", "data wrangling", "etl", "data pipeline",
    "data modeling", "data engineering", "data governance",
    "statistics", "excel", "reporting", "jupyter", "databricks",
    
    # AI & Machine Learning
    "machine learning", "deep learning", "tensorflow", "pytorch",
    "keras", "scikit-learn", "nlp", "computer vision", "opencv",
    "transformers", "bert", "gpt", "llm", "huggingface", "spacy",
    "nltk", "mlops", "mlflow", "kubeflow", "feature engineering",
    "model deployment", "a/b testing", "reinforcement learning",
    
    # Big Data
    "spark", "hadoop", "kafka", "airflow", "hive", "presto",
    "flink", "beam", "dbt", "fivetran", "stitch",
    
    # Security
    "security", "cybersecurity", "penetration testing", "ethical hacking",
    "vulnerability assessment", "siem", "firewalls", "encryption",
    "iam", "zero trust", "compliance", "incident response", "forensics",
    "owasp", "burp suite", "metasploit", "kali linux", "ids/ips",
    "cloud security", "application security", "devsecops",
    
    # Testing & QA
    "testing", "test automation", "selenium", "cypress", "playwright",
    "jest", "junit", "pytest", "rspec", "postman", "api testing",
    "performance testing", "jmeter", "loadrunner", "gatling",
    "manual testing", "regression testing", "unit testing",
    
    # Design
    "ui design", "ux design", "figma", "sketch", "adobe xd",
    "photoshop", "illustrator", "indesign", "after effects",
    "premiere pro", "wireframes", "prototyping", "design systems",
    "typography", "color theory", "responsive design", "ui/ux",
    "user research", "usability testing", "interaction design",
    
    # Project Management & Agile
    "agile", "scrum", "kanban", "jira", "confluence", "trello",
    "asana", "monday", "ms project", "waterfall", "pmp", "prince2",
    "safe", "lean", "six sigma", "sprint planning", "retrospectives",
    
    # Business & Soft Skills
    "leadership", "team management", "stakeholder management",
    "communication", "presentation", "negotiation", "problem solving",
    "strategic planning", "budgeting", "vendor management",
    "requirements gathering", "documentation", "mentoring", "coaching",
    "change management", "risk management", "governance",
    
    # CRM & ERP
    "salesforce", "sap", "oracle", "dynamics", "hubspot", "zoho",
    "netsuite", "workday", "servicenow", "zendesk", "freshdesk",
    "crm", "erp", "quickbooks",
    
    # Marketing & SEO
    "seo", "sem", "google ads", "google analytics", "facebook ads",
    "digital marketing", "content marketing", "email marketing",
    "social media", "marketing automation", "mailchimp", "marketo",
    
    # APIs & Integration
    "rest api", "graphql", "grpc", "soap", "webhooks", "oauth",
    "jwt", "api gateway", "microservices", "event-driven",
    
    # Version Control
    "git", "github", "gitlab", "bitbucket", "svn",
    
    # Game Development
    "unity", "unreal engine", "game design", "3d modeling",
    "graphics programming", "physics",
    
    # Blockchain
    "blockchain", "ethereum", "smart contracts", "web3", "defi", "nft",
    "cryptography",
    
    # Healthcare
    "hipaa", "ehr", "hl7", "fhir", "clinical data", "healthcare it",
    "epic", "cerner", "medical devices", "fda",
    
    # Finance
    "financial modeling", "financial analysis", "valuation",
    "fp&a", "gaap", "ifrs", "sox", "audit", "budgeting",
    "forecasting", "investment analysis", "risk analysis",
    "portfolio management", "m&a", "due diligence",
    
    # HR
    "recruiting", "talent acquisition", "onboarding", "hris",
    "performance management", "compensation", "employee relations",
    "training", "learning & development", "ats",
    
    # Legal & Compliance
    "gdpr", "ccpa", "iso 27001", "pci dss", "regulatory",
    "contracts", "intellectual property", "corporate law",
    
    # Operations
    "operations management", "process improvement", "supply chain",
    "inventory management", "logistics", "procurement", "warehousing",
    "quality assurance", "lean manufacturing",
    
    # Robotics & IoT
    "robotics", "ros", "iot", "embedded systems", "rtos",
    "microcontrollers", "arm", "firmware", "sensors", "arduino",
    "raspberry pi",
    
    # Other Technical
    "algorithms", "data structures", "system design", "architecture",
    "design patterns", "scalability", "high availability",
    "distributed systems", "caching", "load balancing",
    "message queues", "rabbitmq", "sqs",
]


@dataclass(frozen=True)
class SkillExtractionResult:
    """Structured skill extraction output."""

    skills: list[str]
    matches: dict[str, int]


class SkillExtractor:
    """Extract skills from resume text using dictionary and regex patterns."""

    def __init__(self, skill_dictionary: Iterable[str] | None = None) -> None:
        self.skill_dictionary = sorted(
            {skill.lower() for skill in (skill_dictionary or SKILL_DICTIONARY)}
        )
        self._patterns = self._build_patterns()

    def _build_patterns(self) -> dict[str, re.Pattern]:
        patterns: dict[str, re.Pattern] = {}
        for skill in self.skill_dictionary:
            escaped = re.escape(skill)
            pattern = rf"(?<!\w){escaped}(?!\w)"
            patterns[skill] = re.compile(pattern, flags=re.IGNORECASE)
        return patterns

    def extract(self, text: str) -> SkillExtractionResult:
        """Extract skills from text.

        Args:
            text: Cleaned text.

        Returns:
            SkillExtractionResult with unique skills and counts.
        """
        matches: dict[str, int] = {}
        for skill, pattern in self._patterns.items():
            found = pattern.findall(text)
            if found:
                matches[skill] = len(found)

        skills = sorted(matches.keys())
        LOGGER.info("Extracted %d skills", len(skills))
        return SkillExtractionResult(skills=skills, matches=matches)
