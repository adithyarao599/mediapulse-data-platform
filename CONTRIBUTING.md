# Contributing to MediaPulse

Thank you for your interest in contributing to MediaPulse.

## Development Setup

Clone the repository:

```bash
git clone <repository-url>
cd mediapulse-data-platform
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the ingestion pipeline:

```bash
python -m app.ingestion.spotify_ingestor
```

Run Airflow:

```bash
airflow standalone
```

Run tests:

```bash
pytest
```

## Coding Standards

- Follow PEP 8
- Use meaningful variable names
- Keep functions modular
- Add type hints where practical
- Write docstrings for public functions

## Pull Requests

Before submitting a pull request:

- Ensure all tests pass
- Run formatting tools
- Update documentation if required
- Keep commits focused and descriptive

## Reporting Issues

Please include:

- Environment details
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant logs or screenshots

Thank you for helping improve MediaPulse.