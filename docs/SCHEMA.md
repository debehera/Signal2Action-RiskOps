# Database Schema: Signal2Action RiskOps
- **assets:** id, hostname, ip_address, environment, business_criticality
- **applications:** id, name, owner_email, business_service
- **findings:** id, asset_id, source, cve_id, technical_severity, exploit_status, raw_payload, status
- **campaigns:** id, title, scope_description, target_date, status
- **exceptions:** id, finding_id, justification, approved_by, expiry_date