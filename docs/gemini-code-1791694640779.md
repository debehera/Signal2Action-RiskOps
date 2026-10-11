# System Architecture: Signal2Action RiskOps
- **Frontend/API:** FastAPI (Python) hosted on Azure App Service Free Tier.
- **Database:** Azure Database for PostgreSQL Flexible Server.
- **Data Flow:** Ingestion Adapters -> Normalization Engine -> Correlation & Deduplication -> Prioritization & Scorer -> Campaign Orchestrator.