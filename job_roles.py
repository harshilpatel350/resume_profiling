"""Job role definitions with position-specific skills."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class JobRole:
    """A job role with required skills."""
    name: str
    category: str
    skills: list[str]


# =============================================================================
# COMPREHENSIVE JOB ROLES DATABASE
# =============================================================================

JOB_ROLES: list[JobRole] = [

    # =========================================================================
    # DATA & ANALYTICS
    # =========================================================================
    JobRole(
        name="Data Analyst",
        category="Data & Analytics",
        skills=[
            "python", "r", "sql", "excel", "tableau", "power bi",
            "pandas", "numpy", "matplotlib", "seaborn", "statistics",
            "data analysis", "data cleaning", "etl", "reporting",
            "mysql", "postgresql", "bigquery", "looker", "git"
        ]
    ),
    JobRole(
        name="Data Scientist",
        category="Data & Analytics",
        skills=[
            "python", "r", "sql", "pandas", "numpy", "scikit-learn",
            "tensorflow", "pytorch", "keras", "machine learning",
            "deep learning", "nlp", "computer vision", "statistics",
            "matplotlib", "seaborn", "jupyter", "git", "aws", "docker"
        ]
    ),
    JobRole(
        name="Business Analyst",
        category="Data & Analytics",
        skills=[
            "sql", "excel", "tableau", "power bi", "python",
            "data analysis", "reporting", "statistics", "jira",
            "agile", "scrum", "mysql", "postgresql", "looker", "git",
            "requirements gathering", "stakeholder management"
        ]
    ),
    JobRole(
        name="Data Engineer",
        category="Data & Analytics",
        skills=[
            "python", "sql", "spark", "hadoop", "airflow", "kafka",
            "aws", "azure", "gcp", "docker", "kubernetes", "etl",
            "data pipeline", "postgresql", "mongodb", "redshift",
            "snowflake", "databricks", "git", "linux"
        ]
    ),
    JobRole(
        name="Business Intelligence Analyst",
        category="Data & Analytics",
        skills=[
            "sql", "tableau", "power bi", "looker", "excel",
            "data visualization", "reporting", "etl", "python",
            "statistics", "mysql", "postgresql", "bigquery"
        ]
    ),
    JobRole(
        name="Quantitative Analyst",
        category="Data & Analytics",
        skills=[
            "python", "r", "sql", "statistics", "mathematics",
            "machine learning", "financial modeling", "excel",
            "matlab", "c++", "algorithms", "risk analysis"
        ]
    ),
    JobRole(
        name="Analytics Manager",
        category="Data & Analytics",
        skills=[
            "sql", "python", "tableau", "power bi", "statistics",
            "team management", "stakeholder management", "reporting",
            "data strategy", "leadership", "communication"
        ]
    ),

    # =========================================================================
    # SOFTWARE DEVELOPMENT
    # =========================================================================
    JobRole(
        name="Software Engineer",
        category="Software Development",
        skills=[
            "python", "java", "javascript", "c++", "sql", "git",
            "docker", "kubernetes", "aws", "linux", "rest api",
            "agile", "scrum", "unit testing", "ci/cd", "microservices"
        ]
    ),
    JobRole(
        name="Frontend Developer",
        category="Software Development",
        skills=[
            "javascript", "typescript", "react", "angular", "vue",
            "html", "css", "sass", "webpack", "npm", "git",
            "rest api", "responsive design", "ui/ux", "jest"
        ]
    ),
    JobRole(
        name="Backend Developer",
        category="Software Development",
        skills=[
            "python", "java", "node.js", "go", "sql", "postgresql",
            "mongodb", "redis", "docker", "kubernetes", "aws",
            "rest api", "microservices", "git", "linux", "ci/cd"
        ]
    ),
    JobRole(
        name="Full Stack Developer",
        category="Software Development",
        skills=[
            "javascript", "typescript", "python", "react", "node.js",
            "sql", "mongodb", "postgresql", "html", "css", "git",
            "docker", "aws", "rest api", "agile"
        ]
    ),
    JobRole(
        name="Mobile Developer",
        category="Software Development",
        skills=[
            "swift", "kotlin", "react native", "flutter", "java",
            "ios", "android", "mobile development", "git", "rest api",
            "firebase", "app store", "ui/ux"
        ]
    ),
    JobRole(
        name="iOS Developer",
        category="Software Development",
        skills=[
            "swift", "objective-c", "ios", "xcode", "cocoapods",
            "core data", "uikit", "swiftui", "rest api", "git",
            "app store", "mobile development"
        ]
    ),
    JobRole(
        name="Android Developer",
        category="Software Development",
        skills=[
            "kotlin", "java", "android", "android studio", "gradle",
            "room", "retrofit", "jetpack compose", "rest api", "git",
            "google play", "mobile development"
        ]
    ),
    JobRole(
        name="Java Developer",
        category="Software Development",
        skills=[
            "java", "spring", "spring boot", "hibernate", "maven",
            "gradle", "sql", "postgresql", "mysql", "rest api",
            "microservices", "docker", "git", "junit"
        ]
    ),
    JobRole(
        name="Python Developer",
        category="Software Development",
        skills=[
            "python", "django", "flask", "fastapi", "sql",
            "postgresql", "mongodb", "redis", "docker", "git",
            "rest api", "linux", "aws", "pytest"
        ]
    ),
    JobRole(
        name=".NET Developer",
        category="Software Development",
        skills=[
            "c#", ".net", "asp.net", "sql server", "azure",
            "entity framework", "rest api", "git", "visual studio",
            "microservices", "docker", "javascript"
        ]
    ),
    JobRole(
        name="PHP Developer",
        category="Software Development",
        skills=[
            "php", "laravel", "symfony", "mysql", "javascript",
            "html", "css", "rest api", "git", "composer",
            "wordpress", "docker"
        ]
    ),
    JobRole(
        name="Ruby Developer",
        category="Software Development",
        skills=[
            "ruby", "ruby on rails", "postgresql", "mysql", "redis",
            "javascript", "html", "css", "rest api", "git",
            "docker", "heroku", "rspec"
        ]
    ),
    JobRole(
        name="Go Developer",
        category="Software Development",
        skills=[
            "go", "golang", "docker", "kubernetes", "microservices",
            "rest api", "grpc", "postgresql", "mongodb", "redis",
            "git", "linux", "aws", "ci/cd"
        ]
    ),
    JobRole(
        name="Rust Developer",
        category="Software Development",
        skills=[
            "rust", "systems programming", "c++", "linux", "git",
            "docker", "webassembly", "performance optimization",
            "memory management", "concurrency"
        ]
    ),
    JobRole(
        name="Embedded Software Engineer",
        category="Software Development",
        skills=[
            "c", "c++", "embedded systems", "rtos", "linux",
            "microcontrollers", "arm", "firmware", "debugging",
            "hardware", "iot", "git"
        ]
    ),
    JobRole(
        name="Game Developer",
        category="Software Development",
        skills=[
            "unity", "unreal engine", "c#", "c++", "game design",
            "3d modeling", "physics", "graphics programming",
            "git", "agile", "mobile development"
        ]
    ),
    JobRole(
        name="Blockchain Developer",
        category="Software Development",
        skills=[
            "solidity", "ethereum", "smart contracts", "web3",
            "javascript", "python", "cryptography", "defi",
            "nft", "git", "docker", "node.js"
        ]
    ),

    # =========================================================================
    # AI & MACHINE LEARNING
    # =========================================================================
    JobRole(
        name="ML Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "sql", "tensorflow", "pytorch", "keras",
            "scikit-learn", "machine learning", "deep learning",
            "mlops", "docker", "kubernetes", "aws", "azure", "gcp",
            "airflow", "spark", "git", "fastapi", "flask", "ci/cd"
        ]
    ),
    JobRole(
        name="AI Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "tensorflow", "pytorch", "deep learning",
            "machine learning", "nlp", "computer vision", "llm",
            "transformers", "docker", "aws", "git", "mlops"
        ]
    ),
    JobRole(
        name="NLP Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "nlp", "transformers", "bert", "gpt",
            "huggingface", "spacy", "nltk", "tensorflow", "pytorch",
            "machine learning", "deep learning", "git"
        ]
    ),
    JobRole(
        name="Computer Vision Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "computer vision", "opencv", "tensorflow",
            "pytorch", "deep learning", "cnn", "image processing",
            "yolo", "object detection", "git", "docker"
        ]
    ),
    JobRole(
        name="MLOps Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "mlops", "mlflow", "kubeflow", "docker",
            "kubernetes", "aws", "azure", "gcp", "ci/cd",
            "airflow", "terraform", "git", "machine learning"
        ]
    ),
    JobRole(
        name="Research Scientist",
        category="AI & Machine Learning",
        skills=[
            "python", "machine learning", "deep learning", "pytorch",
            "tensorflow", "mathematics", "statistics", "research",
            "publications", "nlp", "computer vision", "git"
        ]
    ),
    JobRole(
        name="AI Research Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "pytorch", "tensorflow", "deep learning",
            "machine learning", "research", "mathematics",
            "algorithms", "cuda", "gpu", "git"
        ]
    ),
    JobRole(
        name="Prompt Engineer",
        category="AI & Machine Learning",
        skills=[
            "llm", "gpt", "prompt engineering", "chatgpt", "openai",
            "langchain", "python", "nlp", "machine learning",
            "api integration", "git"
        ]
    ),
    JobRole(
        name="Robotics Engineer",
        category="AI & Machine Learning",
        skills=[
            "python", "c++", "ros", "robotics", "computer vision",
            "machine learning", "control systems", "sensors",
            "embedded systems", "linux", "git"
        ]
    ),

    # =========================================================================
    # CLOUD & DEVOPS
    # =========================================================================
    JobRole(
        name="DevOps Engineer",
        category="Cloud & DevOps",
        skills=[
            "docker", "kubernetes", "aws", "azure", "gcp", "terraform",
            "ansible", "jenkins", "ci/cd", "linux", "git", "python",
            "bash", "monitoring", "prometheus", "grafana"
        ]
    ),
    JobRole(
        name="Cloud Engineer",
        category="Cloud & DevOps",
        skills=[
            "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
            "cloudformation", "networking", "security", "linux",
            "python", "ci/cd", "git"
        ]
    ),
    JobRole(
        name="AWS Solutions Architect",
        category="Cloud & DevOps",
        skills=[
            "aws", "ec2", "s3", "lambda", "rds", "vpc", "iam",
            "cloudformation", "terraform", "docker", "kubernetes",
            "networking", "security", "architecture"
        ]
    ),
    JobRole(
        name="Azure Solutions Architect",
        category="Cloud & DevOps",
        skills=[
            "azure", "azure devops", "azure functions", "azure sql",
            "azure ad", "arm templates", "terraform", "docker",
            "kubernetes", "networking", "security", "architecture"
        ]
    ),
    JobRole(
        name="GCP Cloud Engineer",
        category="Cloud & DevOps",
        skills=[
            "gcp", "google cloud", "bigquery", "cloud functions",
            "gke", "terraform", "docker", "kubernetes", "networking",
            "security", "python", "linux"
        ]
    ),
    JobRole(
        name="Site Reliability Engineer",
        category="Cloud & DevOps",
        skills=[
            "linux", "python", "go", "docker", "kubernetes", "aws",
            "terraform", "monitoring", "prometheus", "grafana",
            "incident management", "sre", "git", "ci/cd"
        ]
    ),
    JobRole(
        name="Platform Engineer",
        category="Cloud & DevOps",
        skills=[
            "kubernetes", "docker", "terraform", "aws", "azure",
            "ci/cd", "python", "go", "linux", "gitops",
            "argocd", "helm", "infrastructure"
        ]
    ),
    JobRole(
        name="Release Engineer",
        category="Cloud & DevOps",
        skills=[
            "ci/cd", "jenkins", "gitlab", "github actions", "docker",
            "kubernetes", "python", "bash", "git", "release management",
            "automation"
        ]
    ),
    JobRole(
        name="Infrastructure Engineer",
        category="Cloud & DevOps",
        skills=[
            "terraform", "ansible", "aws", "azure", "linux",
            "networking", "docker", "kubernetes", "python",
            "bash", "git", "infrastructure as code"
        ]
    ),
    JobRole(
        name="System Administrator",
        category="Cloud & DevOps",
        skills=[
            "linux", "windows server", "networking", "active directory",
            "vmware", "bash", "powershell", "monitoring", "security",
            "backup", "troubleshooting"
        ]
    ),
    JobRole(
        name="Linux Administrator",
        category="Cloud & DevOps",
        skills=[
            "linux", "bash", "ansible", "docker", "networking",
            "security", "monitoring", "apache", "nginx", "mysql",
            "postgresql", "troubleshooting"
        ]
    ),
    JobRole(
        name="Network Engineer",
        category="Cloud & DevOps",
        skills=[
            "networking", "cisco", "tcp/ip", "dns", "dhcp", "vpn",
            "firewall", "routing", "switching", "load balancing",
            "troubleshooting", "security"
        ]
    ),

    # =========================================================================
    # DATABASE & SQL
    # =========================================================================
    JobRole(
        name="SQL Developer",
        category="Database",
        skills=[
            "sql", "mysql", "postgresql", "sqlite", "mongodb",
            "sql server", "oracle", "bigquery", "etl", "python",
            "data modeling", "database", "git", "aws", "azure"
        ]
    ),
    JobRole(
        name="Database Administrator",
        category="Database",
        skills=[
            "sql", "mysql", "postgresql", "oracle", "sql server",
            "mongodb", "database administration", "backup",
            "performance tuning", "security", "replication", "linux"
        ]
    ),
    JobRole(
        name="Database Developer",
        category="Database",
        skills=[
            "sql", "pl/sql", "t-sql", "postgresql", "mysql",
            "oracle", "sql server", "stored procedures", "etl",
            "data modeling", "performance tuning", "git"
        ]
    ),
    JobRole(
        name="MongoDB Developer",
        category="Database",
        skills=[
            "mongodb", "nosql", "python", "node.js", "aggregation",
            "indexing", "sharding", "replication", "mongoose",
            "database design", "git"
        ]
    ),

    # =========================================================================
    # CYBERSECURITY
    # =========================================================================
    JobRole(
        name="Security Engineer",
        category="Cybersecurity",
        skills=[
            "security", "penetration testing", "vulnerability assessment",
            "siem", "firewalls", "encryption", "python", "linux",
            "networking", "compliance", "incident response"
        ]
    ),
    JobRole(
        name="Cybersecurity Analyst",
        category="Cybersecurity",
        skills=[
            "security", "siem", "threat analysis", "incident response",
            "vulnerability management", "firewalls", "ids/ips",
            "networking", "compliance", "forensics"
        ]
    ),
    JobRole(
        name="Penetration Tester",
        category="Cybersecurity",
        skills=[
            "penetration testing", "ethical hacking", "burp suite",
            "metasploit", "kali linux", "owasp", "python",
            "networking", "web security", "vulnerability assessment"
        ]
    ),
    JobRole(
        name="Security Architect",
        category="Cybersecurity",
        skills=[
            "security architecture", "cloud security", "zero trust",
            "encryption", "identity management", "compliance",
            "risk assessment", "firewalls", "networking", "aws"
        ]
    ),
    JobRole(
        name="SOC Analyst",
        category="Cybersecurity",
        skills=[
            "siem", "incident response", "threat detection",
            "log analysis", "security monitoring", "firewalls",
            "networking", "malware analysis", "splunk"
        ]
    ),
    JobRole(
        name="Information Security Manager",
        category="Cybersecurity",
        skills=[
            "security management", "risk management", "compliance",
            "iso 27001", "gdpr", "team management", "policy",
            "incident response", "vendor management"
        ]
    ),
    JobRole(
        name="Cloud Security Engineer",
        category="Cybersecurity",
        skills=[
            "cloud security", "aws", "azure", "gcp", "iam",
            "encryption", "compliance", "container security",
            "kubernetes", "terraform", "security automation"
        ]
    ),
    JobRole(
        name="Application Security Engineer",
        category="Cybersecurity",
        skills=[
            "application security", "owasp", "sast", "dast",
            "code review", "penetration testing", "python",
            "java", "security testing", "devsecops"
        ]
    ),

    # =========================================================================
    # QA & TESTING
    # =========================================================================
    JobRole(
        name="QA Engineer",
        category="QA & Testing",
        skills=[
            "testing", "test automation", "selenium", "python",
            "java", "api testing", "postman", "jira", "agile",
            "test cases", "bug tracking", "git"
        ]
    ),
    JobRole(
        name="Software Tester",
        category="QA & Testing",
        skills=[
            "manual testing", "test cases", "bug tracking", "jira",
            "regression testing", "functional testing", "agile",
            "test planning", "quality assurance"
        ]
    ),
    JobRole(
        name="Automation Engineer",
        category="QA & Testing",
        skills=[
            "test automation", "selenium", "python", "java",
            "cypress", "playwright", "ci/cd", "api testing",
            "git", "jenkins", "framework development"
        ]
    ),
    JobRole(
        name="Performance Engineer",
        category="QA & Testing",
        skills=[
            "performance testing", "jmeter", "loadrunner", "gatling",
            "monitoring", "analysis", "python", "sql",
            "troubleshooting", "optimization"
        ]
    ),
    JobRole(
        name="SDET",
        category="QA & Testing",
        skills=[
            "test automation", "python", "java", "selenium",
            "api testing", "ci/cd", "docker", "git",
            "programming", "framework development", "agile"
        ]
    ),
    JobRole(
        name="QA Lead",
        category="QA & Testing",
        skills=[
            "test management", "team management", "test strategy",
            "automation", "agile", "jira", "quality assurance",
            "stakeholder management", "reporting"
        ]
    ),

    # =========================================================================
    # UI/UX DESIGN
    # =========================================================================
    JobRole(
        name="UI Designer",
        category="UI/UX Design",
        skills=[
            "ui design", "figma", "sketch", "adobe xd", "photoshop",
            "illustrator", "typography", "color theory", "wireframes",
            "prototyping", "design systems"
        ]
    ),
    JobRole(
        name="UX Designer",
        category="UI/UX Design",
        skills=[
            "ux design", "user research", "wireframes", "prototyping",
            "figma", "usability testing", "information architecture",
            "user flows", "personas", "design thinking"
        ]
    ),
    JobRole(
        name="Product Designer",
        category="UI/UX Design",
        skills=[
            "product design", "ui design", "ux design", "figma",
            "prototyping", "user research", "design systems",
            "interaction design", "agile", "collaboration"
        ]
    ),
    JobRole(
        name="Visual Designer",
        category="UI/UX Design",
        skills=[
            "visual design", "graphic design", "photoshop",
            "illustrator", "figma", "branding", "typography",
            "color theory", "marketing materials"
        ]
    ),
    JobRole(
        name="Interaction Designer",
        category="UI/UX Design",
        skills=[
            "interaction design", "prototyping", "figma", "principle",
            "after effects", "animation", "user flows",
            "microinteractions", "ux design"
        ]
    ),
    JobRole(
        name="UX Researcher",
        category="UI/UX Design",
        skills=[
            "user research", "usability testing", "interviews",
            "surveys", "data analysis", "personas", "user journeys",
            "a/b testing", "qualitative research", "quantitative research"
        ]
    ),
    JobRole(
        name="Design Lead",
        category="UI/UX Design",
        skills=[
            "design leadership", "team management", "design systems",
            "ui design", "ux design", "figma", "stakeholder management",
            "mentoring", "strategy"
        ]
    ),

    # =========================================================================
    # PRODUCT MANAGEMENT
    # =========================================================================
    JobRole(
        name="Product Manager",
        category="Product Management",
        skills=[
            "product management", "roadmap", "agile", "scrum", "jira",
            "stakeholder management", "user research", "data analysis",
            "prioritization", "strategy", "communication"
        ]
    ),
    JobRole(
        name="Technical Product Manager",
        category="Product Management",
        skills=[
            "product management", "technical", "api", "sql", "agile",
            "roadmap", "engineering", "data analysis", "jira",
            "stakeholder management", "architecture"
        ]
    ),
    JobRole(
        name="Product Owner",
        category="Product Management",
        skills=[
            "product owner", "agile", "scrum", "backlog management",
            "user stories", "jira", "stakeholder management",
            "prioritization", "sprint planning"
        ]
    ),
    JobRole(
        name="Associate Product Manager",
        category="Product Management",
        skills=[
            "product management", "agile", "jira", "data analysis",
            "user research", "documentation", "communication",
            "roadmap", "collaboration"
        ]
    ),
    JobRole(
        name="Chief Product Officer",
        category="Product Management",
        skills=[
            "product strategy", "leadership", "team management",
            "stakeholder management", "vision", "roadmap",
            "business strategy", "executive communication"
        ]
    ),

    # =========================================================================
    # PROJECT MANAGEMENT
    # =========================================================================
    JobRole(
        name="Project Manager",
        category="Project Management",
        skills=[
            "project management", "agile", "scrum", "waterfall",
            "jira", "ms project", "stakeholder management",
            "risk management", "budgeting", "scheduling", "pmp"
        ]
    ),
    JobRole(
        name="Technical Project Manager",
        category="Project Management",
        skills=[
            "project management", "technical", "agile", "scrum",
            "jira", "software development", "stakeholder management",
            "risk management", "budgeting", "architecture"
        ]
    ),
    JobRole(
        name="Scrum Master",
        category="Project Management",
        skills=[
            "scrum", "agile", "facilitation", "coaching",
            "jira", "sprint planning", "retrospectives",
            "impediment removal", "team collaboration"
        ]
    ),
    JobRole(
        name="Agile Coach",
        category="Project Management",
        skills=[
            "agile", "scrum", "kanban", "coaching", "facilitation",
            "transformation", "leadership", "team development",
            "safe", "lean"
        ]
    ),
    JobRole(
        name="Program Manager",
        category="Project Management",
        skills=[
            "program management", "project management", "stakeholder management",
            "strategic planning", "risk management", "budgeting",
            "cross-functional", "leadership", "governance"
        ]
    ),
    JobRole(
        name="Portfolio Manager",
        category="Project Management",
        skills=[
            "portfolio management", "strategic planning", "governance",
            "resource management", "budgeting", "stakeholder management",
            "risk management", "leadership"
        ]
    ),
    JobRole(
        name="PMO Director",
        category="Project Management",
        skills=[
            "pmo", "project management", "governance", "leadership",
            "strategic planning", "process improvement", "reporting",
            "stakeholder management", "budgeting"
        ]
    ),

    # =========================================================================
    # IT MANAGEMENT & LEADERSHIP
    # =========================================================================
    JobRole(
        name="Engineering Manager",
        category="IT Management",
        skills=[
            "engineering management", "team management", "agile",
            "hiring", "mentoring", "technical leadership",
            "stakeholder management", "budgeting", "roadmap"
        ]
    ),
    JobRole(
        name="Technical Lead",
        category="IT Management",
        skills=[
            "technical leadership", "architecture", "code review",
            "mentoring", "python", "java", "git", "agile",
            "software design", "team collaboration"
        ]
    ),
    JobRole(
        name="Software Architect",
        category="IT Management",
        skills=[
            "software architecture", "design patterns", "microservices",
            "cloud", "aws", "azure", "docker", "kubernetes",
            "technical leadership", "scalability", "security"
        ]
    ),
    JobRole(
        name="Solutions Architect",
        category="IT Management",
        skills=[
            "solutions architecture", "cloud", "aws", "azure",
            "enterprise architecture", "integration", "stakeholder management",
            "technical leadership", "documentation"
        ]
    ),
    JobRole(
        name="Enterprise Architect",
        category="IT Management",
        skills=[
            "enterprise architecture", "togaf", "strategic planning",
            "cloud", "integration", "governance", "stakeholder management",
            "digital transformation", "roadmap"
        ]
    ),
    JobRole(
        name="VP of Engineering",
        category="IT Management",
        skills=[
            "engineering leadership", "team management", "strategy",
            "hiring", "budgeting", "stakeholder management",
            "executive communication", "organizational development"
        ]
    ),
    JobRole(
        name="CTO",
        category="IT Management",
        skills=[
            "technical strategy", "leadership", "innovation",
            "architecture", "team building", "stakeholder management",
            "budgeting", "executive communication", "vision"
        ]
    ),
    JobRole(
        name="IT Director",
        category="IT Management",
        skills=[
            "it management", "leadership", "budgeting", "strategy",
            "vendor management", "infrastructure", "security",
            "stakeholder management", "governance"
        ]
    ),
    JobRole(
        name="IT Manager",
        category="IT Management",
        skills=[
            "it management", "team management", "budgeting",
            "vendor management", "infrastructure", "helpdesk",
            "stakeholder management", "project management"
        ]
    ),

    # =========================================================================
    # SUPPORT & OPERATIONS
    # =========================================================================
    JobRole(
        name="Technical Support Engineer",
        category="Support & Operations",
        skills=[
            "technical support", "troubleshooting", "customer service",
            "ticketing", "linux", "windows", "networking",
            "documentation", "communication"
        ]
    ),
    JobRole(
        name="IT Support Specialist",
        category="Support & Operations",
        skills=[
            "it support", "helpdesk", "troubleshooting", "windows",
            "active directory", "networking", "hardware",
            "customer service", "ticketing"
        ]
    ),
    JobRole(
        name="Help Desk Technician",
        category="Support & Operations",
        skills=[
            "helpdesk", "customer service", "troubleshooting",
            "windows", "office 365", "ticketing", "hardware",
            "networking", "communication"
        ]
    ),
    JobRole(
        name="NOC Engineer",
        category="Support & Operations",
        skills=[
            "network operations", "monitoring", "troubleshooting",
            "networking", "linux", "windows", "ticketing",
            "incident management", "documentation"
        ]
    ),
    JobRole(
        name="Operations Manager",
        category="Support & Operations",
        skills=[
            "operations management", "team management", "process improvement",
            "monitoring", "incident management", "sla", "reporting",
            "stakeholder management"
        ]
    ),

    # =========================================================================
    # SALES & MARKETING (TECH)
    # =========================================================================
    JobRole(
        name="Technical Sales Engineer",
        category="Sales & Marketing",
        skills=[
            "technical sales", "presales", "solution selling",
            "product demos", "customer engagement", "crm",
            "communication", "technical knowledge", "negotiation"
        ]
    ),
    JobRole(
        name="Sales Engineer",
        category="Sales & Marketing",
        skills=[
            "sales engineering", "presales", "product demos",
            "rfp", "technical presentations", "crm",
            "stakeholder management", "solution design"
        ]
    ),
    JobRole(
        name="Digital Marketing Manager",
        category="Sales & Marketing",
        skills=[
            "digital marketing", "seo", "sem", "google ads",
            "social media", "analytics", "content marketing",
            "email marketing", "marketing automation", "crm"
        ]
    ),
    JobRole(
        name="Marketing Analyst",
        category="Sales & Marketing",
        skills=[
            "marketing analytics", "google analytics", "sql",
            "excel", "data analysis", "reporting", "tableau",
            "a/b testing", "campaign analysis"
        ]
    ),
    JobRole(
        name="Growth Manager",
        category="Sales & Marketing",
        skills=[
            "growth marketing", "analytics", "a/b testing",
            "user acquisition", "retention", "sql", "data analysis",
            "marketing automation", "product marketing"
        ]
    ),
    JobRole(
        name="SEO Specialist",
        category="Sales & Marketing",
        skills=[
            "seo", "keyword research", "content optimization",
            "google analytics", "search console", "link building",
            "technical seo", "content strategy"
        ]
    ),
    JobRole(
        name="Content Marketing Manager",
        category="Sales & Marketing",
        skills=[
            "content marketing", "content strategy", "copywriting",
            "seo", "social media", "analytics", "blogging",
            "email marketing", "brand voice"
        ]
    ),

    # =========================================================================
    # HR & RECRUITMENT (TECH)
    # =========================================================================
    JobRole(
        name="Technical Recruiter",
        category="HR & Recruitment",
        skills=[
            "technical recruiting", "sourcing", "linkedin",
            "interviewing", "ats", "employer branding",
            "negotiation", "communication", "networking"
        ]
    ),
    JobRole(
        name="HR Manager",
        category="HR & Recruitment",
        skills=[
            "hr management", "recruitment", "employee relations",
            "performance management", "compensation", "compliance",
            "onboarding", "training", "hris"
        ]
    ),
    JobRole(
        name="Talent Acquisition Manager",
        category="HR & Recruitment",
        skills=[
            "talent acquisition", "recruitment strategy", "sourcing",
            "employer branding", "team management", "ats",
            "interviewing", "onboarding", "metrics"
        ]
    ),
    JobRole(
        name="HR Business Partner",
        category="HR & Recruitment",
        skills=[
            "hrbp", "employee relations", "performance management",
            "talent management", "change management", "coaching",
            "strategic hr", "compliance"
        ]
    ),
    JobRole(
        name="People Operations Manager",
        category="HR & Recruitment",
        skills=[
            "people operations", "hr management", "hris",
            "process improvement", "employee experience",
            "onboarding", "compliance", "analytics"
        ]
    ),

    # =========================================================================
    # FINANCE & ACCOUNTING
    # =========================================================================
    JobRole(
        name="Financial Analyst",
        category="Finance & Accounting",
        skills=[
            "financial analysis", "excel", "financial modeling",
            "budgeting", "forecasting", "reporting", "sql",
            "powerpoint", "variance analysis", "erp"
        ]
    ),
    JobRole(
        name="FP&A Analyst",
        category="Finance & Accounting",
        skills=[
            "fp&a", "financial planning", "budgeting", "forecasting",
            "excel", "financial modeling", "reporting", "sql",
            "variance analysis", "erp"
        ]
    ),
    JobRole(
        name="Accountant",
        category="Finance & Accounting",
        skills=[
            "accounting", "gaap", "journal entries", "reconciliation",
            "excel", "financial statements", "erp", "quickbooks",
            "accounts payable", "accounts receivable"
        ]
    ),
    JobRole(
        name="Financial Controller",
        category="Finance & Accounting",
        skills=[
            "financial control", "accounting", "gaap", "reporting",
            "budgeting", "audit", "team management", "compliance",
            "erp", "financial statements"
        ]
    ),
    JobRole(
        name="CFO",
        category="Finance & Accounting",
        skills=[
            "financial leadership", "strategy", "investor relations",
            "fundraising", "m&a", "budgeting", "compliance",
            "team management", "executive communication"
        ]
    ),
    JobRole(
        name="Investment Analyst",
        category="Finance & Accounting",
        skills=[
            "investment analysis", "financial modeling", "valuation",
            "excel", "research", "due diligence", "portfolio management",
            "financial statements", "market analysis"
        ]
    ),
    JobRole(
        name="Risk Analyst",
        category="Finance & Accounting",
        skills=[
            "risk analysis", "risk management", "financial modeling",
            "excel", "statistics", "compliance", "reporting",
            "sql", "data analysis"
        ]
    ),

    # =========================================================================
    # CONSULTING
    # =========================================================================
    JobRole(
        name="Management Consultant",
        category="Consulting",
        skills=[
            "consulting", "strategy", "problem solving", "excel",
            "powerpoint", "stakeholder management", "data analysis",
            "project management", "communication", "research"
        ]
    ),
    JobRole(
        name="Technology Consultant",
        category="Consulting",
        skills=[
            "technology consulting", "digital transformation",
            "architecture", "stakeholder management", "project management",
            "cloud", "agile", "communication", "problem solving"
        ]
    ),
    JobRole(
        name="Strategy Consultant",
        category="Consulting",
        skills=[
            "strategy", "market analysis", "financial modeling",
            "excel", "powerpoint", "research", "stakeholder management",
            "problem solving", "communication"
        ]
    ),
    JobRole(
        name="Data Consultant",
        category="Consulting",
        skills=[
            "data consulting", "data strategy", "analytics",
            "sql", "python", "tableau", "stakeholder management",
            "data governance", "architecture"
        ]
    ),
    JobRole(
        name="SAP Consultant",
        category="Consulting",
        skills=[
            "sap", "sap implementation", "abap", "sap hana",
            "business process", "configuration", "integration",
            "project management", "stakeholder management"
        ]
    ),
    JobRole(
        name="Salesforce Consultant",
        category="Consulting",
        skills=[
            "salesforce", "salesforce administration", "apex",
            "lightning", "integration", "crm", "configuration",
            "project management", "stakeholder management"
        ]
    ),

    # =========================================================================
    # HEALTHCARE IT
    # =========================================================================
    JobRole(
        name="Healthcare Data Analyst",
        category="Healthcare IT",
        skills=[
            "healthcare analytics", "sql", "python", "excel",
            "tableau", "hipaa", "ehr", "clinical data",
            "statistics", "reporting"
        ]
    ),
    JobRole(
        name="Health Informatics Specialist",
        category="Healthcare IT",
        skills=[
            "health informatics", "ehr", "hl7", "fhir", "hipaa",
            "clinical workflows", "data analysis", "sql",
            "healthcare it", "interoperability"
        ]
    ),
    JobRole(
        name="Clinical Systems Analyst",
        category="Healthcare IT",
        skills=[
            "clinical systems", "ehr", "epic", "cerner",
            "healthcare it", "requirements gathering", "sql",
            "testing", "workflow optimization"
        ]
    ),
    JobRole(
        name="Biomedical Engineer",
        category="Healthcare IT",
        skills=[
            "biomedical engineering", "medical devices", "fda",
            "quality assurance", "r&d", "matlab", "python",
            "testing", "documentation"
        ]
    ),

    # =========================================================================
    # EDUCATION & TRAINING
    # =========================================================================
    JobRole(
        name="Technical Trainer",
        category="Education & Training",
        skills=[
            "technical training", "curriculum development",
            "presentation", "instructional design", "e-learning",
            "communication", "documentation", "workshops"
        ]
    ),
    JobRole(
        name="Learning & Development Manager",
        category="Education & Training",
        skills=[
            "learning & development", "training programs",
            "curriculum development", "lms", "team management",
            "budgeting", "stakeholder management", "e-learning"
        ]
    ),
    JobRole(
        name="Instructional Designer",
        category="Education & Training",
        skills=[
            "instructional design", "e-learning", "curriculum development",
            "articulate", "captivate", "lms", "adult learning",
            "storyboarding", "multimedia"
        ]
    ),
    JobRole(
        name="Technical Writer",
        category="Education & Training",
        skills=[
            "technical writing", "documentation", "api documentation",
            "user guides", "markdown", "git", "editing",
            "information architecture", "communication"
        ]
    ),

    # =========================================================================
    # LEGAL & COMPLIANCE
    # =========================================================================
    JobRole(
        name="Legal Counsel",
        category="Legal & Compliance",
        skills=[
            "legal", "contracts", "negotiation", "compliance",
            "corporate law", "intellectual property", "risk management",
            "documentation", "communication"
        ]
    ),
    JobRole(
        name="Compliance Manager",
        category="Legal & Compliance",
        skills=[
            "compliance", "regulatory", "risk management", "audit",
            "policy", "gdpr", "sox", "training",
            "stakeholder management"
        ]
    ),
    JobRole(
        name="Privacy Officer",
        category="Legal & Compliance",
        skills=[
            "data privacy", "gdpr", "ccpa", "hipaa", "compliance",
            "policy", "risk assessment", "training",
            "stakeholder management"
        ]
    ),
    JobRole(
        name="Contract Manager",
        category="Legal & Compliance",
        skills=[
            "contract management", "negotiation", "legal",
            "vendor management", "compliance", "risk management",
            "documentation", "communication"
        ]
    ),

    # =========================================================================
    # OPERATIONS & SUPPLY CHAIN
    # =========================================================================
    JobRole(
        name="Operations Analyst",
        category="Operations & Supply Chain",
        skills=[
            "operations analysis", "process improvement", "excel",
            "sql", "data analysis", "reporting", "lean",
            "six sigma", "project management"
        ]
    ),
    JobRole(
        name="Supply Chain Analyst",
        category="Operations & Supply Chain",
        skills=[
            "supply chain", "inventory management", "excel",
            "sql", "erp", "forecasting", "logistics",
            "data analysis", "reporting"
        ]
    ),
    JobRole(
        name="Logistics Manager",
        category="Operations & Supply Chain",
        skills=[
            "logistics", "supply chain", "inventory management",
            "vendor management", "transportation", "warehousing",
            "team management", "budgeting", "erp"
        ]
    ),
    JobRole(
        name="Procurement Manager",
        category="Operations & Supply Chain",
        skills=[
            "procurement", "vendor management", "negotiation",
            "contracts", "supply chain", "budgeting", "erp",
            "cost reduction", "stakeholder management"
        ]
    ),
    JobRole(
        name="COO",
        category="Operations & Supply Chain",
        skills=[
            "operations leadership", "strategy", "team management",
            "process improvement", "budgeting", "stakeholder management",
            "executive communication", "scaling"
        ]
    ),

    # =========================================================================
    # CUSTOMER SUCCESS
    # =========================================================================
    JobRole(
        name="Customer Success Manager",
        category="Customer Success",
        skills=[
            "customer success", "account management", "onboarding",
            "retention", "upselling", "crm", "communication",
            "stakeholder management", "product knowledge"
        ]
    ),
    JobRole(
        name="Customer Support Manager",
        category="Customer Success",
        skills=[
            "customer support", "team management", "ticketing",
            "kpi", "process improvement", "training",
            "escalation management", "communication"
        ]
    ),
    JobRole(
        name="Account Manager",
        category="Customer Success",
        skills=[
            "account management", "relationship building", "upselling",
            "retention", "crm", "communication", "negotiation",
            "stakeholder management"
        ]
    ),
    JobRole(
        name="Implementation Specialist",
        category="Customer Success",
        skills=[
            "implementation", "onboarding", "training", "project management",
            "customer success", "technical support", "documentation",
            "communication"
        ]
    ),

    # =========================================================================
    # EXECUTIVE & C-SUITE
    # =========================================================================
    JobRole(
        name="CEO",
        category="Executive",
        skills=[
            "leadership", "strategy", "vision", "fundraising",
            "investor relations", "board management", "team building",
            "executive communication", "culture"
        ]
    ),
    JobRole(
        name="CIO",
        category="Executive",
        skills=[
            "it leadership", "digital transformation", "strategy",
            "budgeting", "vendor management", "team management",
            "stakeholder management", "governance"
        ]
    ),
    JobRole(
        name="CISO",
        category="Executive",
        skills=[
            "security leadership", "risk management", "compliance",
            "security strategy", "team management", "incident response",
            "stakeholder management", "governance"
        ]
    ),
    JobRole(
        name="CDO",
        category="Executive",
        skills=[
            "data leadership", "data strategy", "analytics",
            "data governance", "team management", "stakeholder management",
            "machine learning", "digital transformation"
        ]
    ),
    JobRole(
        name="CMO",
        category="Executive",
        skills=[
            "marketing leadership", "brand strategy", "digital marketing",
            "team management", "budgeting", "stakeholder management",
            "growth", "analytics"
        ]
    ),

    # =========================================================================
    # CONTENT & MEDIA
    # =========================================================================
    JobRole(
        name="Content Writer",
        category="Content & Media",
        skills=[
            "content writing", "copywriting", "seo", "blogging",
            "editing", "research", "social media", "cms",
            "storytelling"
        ]
    ),
    JobRole(
        name="Copywriter",
        category="Content & Media",
        skills=[
            "copywriting", "advertising", "brand voice", "seo",
            "email marketing", "social media", "creative writing",
            "editing"
        ]
    ),
    JobRole(
        name="Video Editor",
        category="Content & Media",
        skills=[
            "video editing", "premiere pro", "after effects",
            "final cut", "color grading", "motion graphics",
            "storytelling", "audio editing"
        ]
    ),
    JobRole(
        name="Social Media Manager",
        category="Content & Media",
        skills=[
            "social media", "content strategy", "community management",
            "analytics", "advertising", "copywriting",
            "engagement", "scheduling tools"
        ]
    ),
    JobRole(
        name="Graphic Designer",
        category="Content & Media",
        skills=[
            "graphic design", "photoshop", "illustrator", "indesign",
            "branding", "typography", "color theory", "print design",
            "digital design"
        ]
    ),

    # =========================================================================
    # RESEARCH & ACADEMIA
    # =========================================================================
    JobRole(
        name="Research Engineer",
        category="Research & Academia",
        skills=[
            "research", "python", "machine learning", "deep learning",
            "publications", "mathematics", "algorithms", "pytorch",
            "tensorflow", "experimentation"
        ]
    ),
    JobRole(
        name="Research Analyst",
        category="Research & Academia",
        skills=[
            "research", "data analysis", "excel", "statistics",
            "reporting", "writing", "presentations", "surveys",
            "market research"
        ]
    ),
    JobRole(
        name="Data Research Scientist",
        category="Research & Academia",
        skills=[
            "research", "data science", "python", "r", "statistics",
            "machine learning", "publications", "experimentation",
            "analysis"
        ]
    ),

    # =========================================================================
    # STARTUP & ENTREPRENEURSHIP
    # =========================================================================
    JobRole(
        name="Startup Founder",
        category="Startup",
        skills=[
            "entrepreneurship", "leadership", "fundraising", "strategy",
            "product development", "sales", "marketing", "hiring",
            "vision", "resilience"
        ]
    ),
    JobRole(
        name="Venture Analyst",
        category="Startup",
        skills=[
            "venture capital", "financial modeling", "due diligence",
            "market research", "valuation", "excel", "powerpoint",
            "deal flow", "portfolio management"
        ]
    ),
    JobRole(
        name="Growth Hacker",
        category="Startup",
        skills=[
            "growth hacking", "analytics", "a/b testing", "marketing",
            "product", "sql", "automation", "user acquisition",
            "retention", "viral marketing"
        ]
    ),
]


def get_roles_by_category(category: str) -> list[JobRole]:
    """Get all roles in a specific category."""
    return [role for role in JOB_ROLES if role.category == category]


def get_all_categories() -> list[str]:
    """Get list of all unique categories."""
    return sorted(set(role.category for role in JOB_ROLES))
