from typing import Dict, Any

class FindingNormalizer:
    """
    Normalizes raw security findings and EOL inventory records into a common enterprise schema.
    """
    @staticmethod
    def normalize(parsed_record: Dict[str, Any]) -> Dict[str, Any]:
        severity_mapping = {
            "Critical": 4,
            "High": 3,
            "Medium": 2,
            "Low": 1,
            "Info": 0
        }
        
        tech_sev = parsed_record.get("technical_severity", "Medium")
        numeric_score = severity_mapping.get(tech_sev, 2)

        return {
            "source": parsed_record.get("source"),
            "external_id": parsed_record.get("external_id"),
            "asset_identifier": parsed_record.get("asset_identifier", "UNKNOWN-ASSET"),
            "cve_id": parsed_record.get("cve_id", "N/A"),
            "technical_severity": tech_sev,
            "severity_score": numeric_score,
            "exploit_status": parsed_record.get("exploit_status", False),
            "status": "OPEN",
            "raw_payload": parsed_record.get("raw_payload", {})
        }