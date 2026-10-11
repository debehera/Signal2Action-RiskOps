# Architecture Principles: Signal2Action RiskOps

## Principle 1: Transparency in Risk & Priority
* **Statement:** All risk scores and priority rankings must be fully explainable using transparent formulas rather than black-box algorithms.
* **Rationale:** Security teams and application owners must understand *why* a campaign is prioritized based on technical severity, exploitation status, internet exposure, and business criticality[cite: 1].

## Principle 2: Modular Ingestion & Normalization
* **Statement:** Data ingestion connectors must be decoupled from the core correlation engine via a standardized common data model.
* **Rationale:** Allows seamless addition of new security scanners, EOL feeds, and cloud security assessments without rewriting core business logic[cite: 1].

## Principle 3: Action-Oriented Remediation Over Alert Overload
* **Statement:** The architecture must transform individual alerts into cohesive, executable remediation campaigns with assigned owners and validation evidence[cite: 1].
* **Rationale:** Reduces ticket duplication and ensures vulnerabilities are closed only after verified technical revalidation[cite: 1].

## Principle 4: Cloud-Native Cost Efficiency
* **Statement:** The system architecture must adhere strictly to free-tier and lightweight cloud-native building blocks.
* **Rationale:** Ensures rapid prototyping and deployment on Azure without incurring infrastructure overhead during the 10-day capstone.