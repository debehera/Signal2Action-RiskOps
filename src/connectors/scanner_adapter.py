import json
from typing import List, Dict, Any

class VulnerabilityScannerAdapter:
    """
    Adapter to parse and ingest raw payloads from vulnerability scanners.
    """
    @staticmethod
    def parse_payload(raw_data: str) -> List[Dict[str, Any]]:
        try:
            findings = json.loads(raw_data)
            parsed_findings = []
            for item in findings:
                parsed_findings.append({
                    "source": "vulnerability_scanner",
                    "external_id": item.get("id", "UNKNOWN"),
                    "asset_identifier": item.get("host") or item.get("ip_address"),
                    "cve_id": item.get("cve", "N/A"),
                    "technical_severity": item.get("severity", "Medium"),
                    "exploit_status": item.get("is_exploited", False),
                    "raw_payload": item
                })
            return parsed_findings
        except Exception as e:
            raise ValueError(f"Failed to parse vulnerability scanner payload: {str(e)}")