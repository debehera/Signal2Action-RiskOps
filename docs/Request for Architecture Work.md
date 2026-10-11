# Request for Architecture Work: Signal2Action RiskOps

## 1. Sponsor & Stakeholder Details
* **Sponsor:** Enterprise Chief Information Security Officer (CISO) & Head of Information Security
* **Initiating Organization:** Enterprise Security Operations & IT Infrastructure Directorate
* **Date of Request:** October 2026

## 2. Project Intent & Background
Enterprise security and IT teams currently receive vulnerability findings, EOL notifications, and configuration alerts across fragmented channels (scanners, SIEMs, EDRs, audit logs, and emails)[cite: 1]. Each system generates isolated severities and duplicate tickets, leading to alert fatigue, disputed asset ownership, and disconnection between technical severity and business impact[cite: 1].

## 3. Objective & Desired Business Outcome
The objective is to establish an exposure-to-remediation orchestration platform (**Signal2Action RiskOps**) that ingests multi-channel findings (specifically focusing on vulnerability scanners and EOL inventories), normalizes them, correlates duplicates, and prioritizes them into executable remediation campaigns[cite: 1].

## 4. Scope & Boundaries
* **In-Scope:** Ingestion of vulnerability scanner payloads and EOL inventory files; common finding schema normalization; duplicate detection and deduplication; explainable priority scoring and Remediation Confidence Scoring; automated remediation campaign creation[cite: 1].
* **Out-of-Scope for MVP:** Full SIEM integration, active EDR orchestration, and custom ticketing integrations beyond core REST APIs (to be handled in future phases).

## 5. Timeframe & Resource Constraints
* **Execution Window:** 10-Day Capstone Sprint.
* **Technology Constraints:** Must utilize Azure Free Tier cloud-native resources (Azure App Service and Azure Database for PostgreSQL Flexible Server).