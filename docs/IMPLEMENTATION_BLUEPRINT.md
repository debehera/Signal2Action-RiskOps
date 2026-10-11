# Implementation Blueprint (Days 2–10)
*Single Source of Truth for the 10-Day Capstone Sprint on Azure Free Tier.*

| Day | Phase | Core Engineering Tasks & Architecture Focus | Deliverables & Verification |
| :--- | :--- | :--- | :--- |
| **Day 2** | **Setup & Infrastructure** | Provision Azure Free Tier environment (Azure App Service free tier, Azure Database for PostgreSQL flexible server). Initialize repository and database schema. | Running PostgreSQL instance & FastAPI skeleton deployed. |
| **Day 3** | **Data Ingestion** | Build connector adapters for vulnerability scanner payloads (JSON/CSV) and EOL inventory files. | Raw ingestion pipeline storing payloads in database staging tables. |
| **Day 4** | **Normalization Engine** | Implement the common finding schema parser to map disparate scanner/EOL attributes into uniform data models. | Unit tests validating data mapping accuracy. |
| **Day 5** | **Correlation & Deduplication** | Code the correlation logic to merge duplicate findings and map assets to applications and owners[cite: 1]. | Deduplication query engine successfully grouping multi-source alerts. |
| **Day 6** | **Prioritization & Scoring** | Implement the transparency priority rule engine (JSON/YAML policies) and the Remediation Confidence Score calculation[cite: 1]. | Scored and ranked vulnerability output dataset. |
| **Day 7** | **Campaign Orchestration** | Build campaign creation logic that transforms prioritized clusters into actionable work packages with scopes and target dates[cite: 1]. API endpoint for campaign generation. | Functional API generating structured remediation campaigns. |
| **Day 8** | **Exception & Evidence Handling** | Implement exception approval workflows with expiry tracking and automated evidence upload handlers[cite: 1]. | Exception lifecycle managed via API endpoints. |
| **Day 9** | **Integration & Dashboard** | Build a lightweight dashboard (Streamlit or React on Azure) or Power BI export summarizing weekly management metrics[cite: 1]. | End-to-end visualization of campaigns and risk metrics. |
| **Day 10** | **Testing & Capstone Review** | Perform end-to-end simulation testing, documentation finalization, and pitch deck preparation. | Complete capstone package and deployment verification report. |