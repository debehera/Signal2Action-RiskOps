import json
from typing import List, Dict, Any

class EOLInventoryAdapter:
    """
    Adapter to parse and ingest End-Of-Life (EOL) software/hardware inventory feeds.
    """
    @staticmethod
    def parse_payload(raw_data: str) -> List[Dict[str, Any]]:
        try:
            records = json.loads(raw_data)
            parsed_eol = []
            for item in records:
                parsed_eol.append({
                    "source": "eol_inventory",
                    "external_id": item.get("asset_id", "EOL-UNKNOWN"),
                    "asset_identifier": item.get("hostname") or item.get("ip_address"),
                    "cve_id": item.get("associated_cve", "EOL-RISK"),
                    "technical_severity": "High" if item.get("is_unsupported", True) else "Medium",
                    "exploit_status": False,
                    "raw_payload": item
                })
            return parsed_eol
        except Exception as e:
            raise ValueError(f"Failed to parse EOL inventory payload: {str(e)}")