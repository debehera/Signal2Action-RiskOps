# Product Requirements Document (PRD): Signal2Action RiskOps

## Document Control & Architecture Metadata
* **Project Name:** Signal2Action RiskOps[cite: 1]
* **TOGAF Phase Alignment:** Phase A (Architecture Vision) & Phase B/C (Business & Information Systems Architectures)
* **Target Audience:** CISO, Enterprise Security Team, IT Operations[cite: 1]
* **Execution Window:** 10-Day Capstone Sprint

## Executive Summary & Problem Definition
Enterprise security and IT teams are overwhelmed by fragmented alert streams from vulnerability scanners, EOL inventories, SIEMs, and ticketing systems[cite: 1]. Each channel creates isolated severities, duplicates effort, separates risk severity from business impact, and forces manual evidence collection[cite: 1]. Signal2Action RiskOps addresses this by ingesting multi-channel findings, normalizing them into a common schema, correlating duplicates, and prioritizing them into unified, executable remediation campaigns[cite: 1].

## Functional Requirements (TOGAF Building Blocks)
* **FR-01: Ingestion & Normalization Service**
  * Ingest raw security findings from vulnerability scanners and EOL inventories via APIs or scheduled files[cite: 1].
  * Map disparate formats into a common enterprise data model capturing Asset, Application, CVE/Control Failure, Environment, Owner, Business Service, Exploit Status, and Remediation State[cite: 1].
* **FR-02: Correlation & Deduplication Engine**
  * Merge duplicate findings based on asset, software, CVE, and source[cite: 1].
  * Link vulnerable servers or assets to their respective applications, owners, services, and business criticality[cite: 1].
* **FR-03: Explainable Risk & Confidence Scoring**
  * Apply a transparent priority formula incorporating technical severity, known exploitation, internet exposure, production status, EOL status, and business criticality[cite: 1].
  * Introduce a **Remediation Confidence Score** to measure certainty of safe fix implementation (evaluating patch availability, rollback readiness, and test evidence)[cite: 1].
* **FR-04: Remediation Campaign Orchestration**
  * Group related vulnerabilities into single logical campaigns with scope, affected assets, recommended fixes, and target completion dates[cite: 1].
  * Automate follow-through, exception management with expiry dates, and evidence attachment upon validation[cite: 1].