# Architecture Vision Document: Signal2Action RiskOps

## 1. Business Goals & Vision
To transition enterprise security from reactive, fragmented alert firefighting into proactive, campaign-driven remediation orchestration[cite: 1]. Signal2Action RiskOps bridges the gap between technical vulnerability data and business service impact[cite: 1].

## 2. Problem Summary
* Fragmented alert channels (scanners, EOL reports, SIEMs) create severe alert fatigue[cite: 1].
* Teams waste effort investigating duplicate findings[cite: 1].
* Risk severity is disconnected from true business context and asset criticality[cite: 1].

## 3. Target Architecture Summary
* **Ingestion:** Automated pull/push of vulnerability and EOL feeds[cite: 1].
* **Normalization & Correlation:** Unified schema merging duplicates and linking assets to application owners[cite: 1].
* **Orchestration:** Actionable campaigns grouping patches, fixes, and evidence requirements into unified work packages[cite: 1].