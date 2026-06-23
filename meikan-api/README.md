# Meikan API

Backend service for **Meikan**, a portfolio and profile directory platform.

## Motivation

Meikan separates content from presentation.

A single API acts as the source of truth for portfolio data, allowing multiple 
clients, such as a website and TUI, to consume the same content without duplication.

## Tech Stack

- **Python 3.14**
- **FastAPI** for the web framework
- **Pydantic** for data validation and serialization
- **Pytest** for testing
- **Ruff** for linting and formatting
- **UV** for dependency management and execution
- **GitHub Actions** for CI
- **Google Cloud Run** (planned) for deployment

## Project Structure

```text
meikan-api/
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── main.py
├── tests/
├── pyproject.toml
└── Makefile
```

### Prerequisites

1. Python 3.14+
2. UV
3. Make

## Getting Started

1. Install Dependencies

```bash
uv sync
```

2. Run the Development Server

```bash
make run
```

3. Running Tests

```bash
make test
```


4. Linting

```bash
make lint
```

5. Formatting

```bash
make format
```

6. Running All Checks

```bash
make check
```
