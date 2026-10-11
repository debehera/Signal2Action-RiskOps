# Statement of Architecture Work: Signal2Action RiskOps

## 1. Project Title & Overview
**Signal2Action RiskOps:** Exposure-to-Remediation Orchestration Platform[cite: 1].

## 2. Scope of Work
The architect shall deliver a fully functional backend and data pipeline prototype within 10 days, encompassing:
1. Data ingestion adapters for vulnerability scanners and EOL inventories[cite: 1].
2. A common finding normalization schema[cite: 1].
3. Deduplication and asset-to-application correlation logic[cite: 1].
4. Transparent priority scoring and Remediation Confidence Scoring[cite: 1].
5. Remediation campaign generation and exception management endpoints[cite: 1].

## 3. Deliverables Schedule
* **Days 1–2:** Vision framing, system design, database schema, and API specification.
* **Days 3–6:** Core engineering of ingestion, normalization, correlation, and scoring engines.
* **Days 7–9:** Campaign orchestration, exception handling, and dashboard integration.
* **Day 10:** End-to-end testing, documentation finalization, and pitch deck review.

## 4. Acceptance Criteria
* Successful ingestion and parsing of multi-channel scanner/EOL payloads.
* Elimination of duplicate findings through asset/CVE correlation.
* Generation of structured remediation campaigns ready for application owner review.