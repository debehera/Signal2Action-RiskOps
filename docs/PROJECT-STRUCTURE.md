# Project Structure Guide

```text
Signal2Action-RiskOps/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions for automated testing
├── docs/                          # TOGAF & Project Documentation
│   ├── PRD.md
│   ├── IMPLEMENTATION_BLUEPRINT.md
│   ├── TOGAF_ARCHITECTURE.md
│   ├── PITCH_DECK.md
│   ├── SETUP.md
│   ├── ENVIRONMENT.md
│   └── PROJECT-STRUCTURE.md
│
├── src/                           # Application Source Code
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI entrypoint
│   │   └── routes.py              # API endpoints for campaigns & findings
│   ├── connectors/
│   │   ├── __init__.py
│   │   ├── scanner_adapter.py     # Vulnerability scanner parser
│   │   └── eol_adapter.py         # EOL inventory parser
│   ├── core/
│   │   ├── __init__.py
│   │   ├── normalizer.py          # Common finding schema mapping
│   │   ├── correlator.py          # Duplicate merging & asset mapping
│   │   └── scorer.py              # Priority & confidence scoring rules
│   └── database/
│       ├── __init__.py
│       └── database.py            # Database session management
│       └── models.py              # SQLAlchemy database models
│
├── tests/                         # Unit and integration test suite
│   ├── test_normalizer.py
│   └── test_correlator.py
│
├── .env.example                   # Sample environment variables
├── requirements.txt               # Python dependencies (FastAPI, SQLAlchemy, etc.)
├── Dockerfile                     # Containerization setup for Azure
└── README.md                      # Project overview and run instructions