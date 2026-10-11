# TOGAF Architecture Artifacts & Documents

## 1. Business Architecture (Phase B)
* **Actor-Role Matrix:** 
  * *CISO / Risk Manager:* Defines risk policies, reviews weekly management summaries, and approves high-level exceptions.
  * *Security Operations Analyst:* Manages ingestion feeds, monitors correlation outputs, and verifies remediation evidence.
  * *Application Owner:* Receives remediation campaigns, plans maintenance windows, and submits validation evidence.
* **Business Interaction Diagram Summary:** Illustrates the seamless hand-off from automated vulnerability ingestion to human-verified campaign closure and audit logging.

## 2. Information Systems Architecture (Phase C)
* **Data Entity Relationship (ERD) Schema:**
  * `Asset`: ID, hostname, IP, environment, business criticality.
  * `Application`: ID, name, owner, business service.
  * `Finding`: ID, source, CVE/control ID, technical severity, exploit status, raw payload.
  * `Campaign`: ID, title, scope, target remediation date, status.
  * `Exception`: ID, justification, approved_by, expiry_date.
* **Application Communication Diagram:** Details RESTful API exchanges between Ingestion Adapters, the Core Correlation Service, and the PostgreSQL Datastore.

## 3. Technology Architecture (Phase D)
* **Deployment Topology:** Maps FastAPI backend microservices and PostgreSQL database onto Azure Free Tier resources (Azure App Service + Azure Database for PostgreSQL Flexible Server).