# Customized Architecture Framework: Signal2Action RiskOps

## 1. Framework Adaptation
This framework adapts the TOGAF Standard (Version 10) Architecture Content Framework and ADM cycle to a compressed **10-day enterprise security capstone project**.

## 2. Tailored TOGAF ADM Phases
* **Preliminary Phase:** Establishes architecture governance, guiding principles, and project repository structures.
* **Phase A (Architecture Vision):** Defines the problem statement, ingestion boundaries (vulnerability scanners and EOL inventories), stakeholders, and cloud-native target environment (Azure Free Tier)[cite: 1].
* **Phase B (Business Architecture):** Maps actor-role matrices (CISO, Security Analyst, Application Owner) and workflow hand-offs.
* **Phase C (Information Systems Architecture):** Defines data entities (`Asset`, `Application`, `Finding`, `Campaign`, `Exception`) and RESTful API communications.
* **Phase D (Technology Architecture):** Specifies the deployment topology utilizing FastAPI and PostgreSQL on Azure.

## 3. Architecture Deliverables Registry
* PRD & Implementation Blueprint (`docs/PRD.md`, `docs/IMPLEMENTATION_BLUEPRINT.md`)
* System Architecture & Schema (`docs/ARCHITECTURE.md`, `docs/SCHEMA.md`)
* API & UI Specifications (`docs/API.md`, `docs/UI-WIREFRAMES.md`)