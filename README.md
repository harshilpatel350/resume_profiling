# Resume Profiling

A production-quality Python system that accepts resumes in multiple formats, extracts text, analyzes candidate skills, compares them with job descriptions, and generates structured skill gap reports.

## Features
- Universal file support: TXT, PDF, DOCX, JSON, PNG/JPG (OCR)
- Modular extractor architecture
- Text normalization and skill extraction
- Job description analysis
- Skill matching and scoring
- Report generation (JSON and TXT)
- CLI interface
- Logging and error handling

## Installation
1. Ensure Python 3.10+ is installed.
2. Install dependencies:
   - `pip install -r requirements.txt`

## Usage
Run the CLI with resume and job description files:
- `python -m resume_profiling.main --resume data_samples/sample_resume.txt --job data_samples/sample_job.txt`

Optional arguments:
- `--output` Output directory for reports
- `--log` Custom log file path

Reports generated:
- `analysis_report.json`
- `analysis_report.txt`

## Architecture Diagram (ASCII)

```
+------------------+     +-------------------+     +-------------------+
|  File Detector   | --> |  Extractor Router | --> |  Text Cleaner     |
+------------------+     +-------------------+     +-------------------+
                                                           |
                                                           v
          +-------------------+     +-------------------+   +-------------------+
          |  Skill Extractor  | --> |  Skill Matcher    |-->|  Scoring Engine   |
          +-------------------+     +-------------------+   +-------------------+
                    ^                        |
                    |                        v
          +-------------------+     +-------------------+
          |   Job Parser      | --> | Report Generator  |
          +-------------------+     +-------------------+
```

## Testing
Run tests from the project root:
- `python -m unittest resume_profiling.tests.test_sample`

## Future Improvements
- Add language detection and multilingual skill parsing
- Add configurable skill taxonomies per domain
- Introduce embedding-based semantic similarity
- Add structured output for ATS systems
