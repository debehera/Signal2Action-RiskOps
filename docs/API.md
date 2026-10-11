# API Specification: Signal2Action RiskOps v1.0
- POST /api/v1/findings/ingest - Ingest raw scanner/EOL feeds
- POST /api/v1/correlate - Run deduplication and asset mapping
- GET /api/v1/campaigns - List active remediation campaigns
- POST /api/v1/exceptions - Submit risk exceptions with expiry