import json
from src.connectors.scanner_adapter import VulnerabilityScannerAdapter
from src.connectors.eol_adapter import EOLInventoryAdapter

def test_scanner_adapter_parsing():
    raw_payload = json.dumps([
        {
            "id": "SCAN-101",
            "host": "web-prod-01",
            "cve": "CVE-2024-5678",
            "severity": "High",
            "is_exploited": True
        }
    ])

    results = VulnerabilityScannerAdapter.parse_payload(raw_payload)

    assert len(results) == 1
    assert results[0]["external_id"] == "SCAN-101"
    assert results[0]["asset_identifier"] == "web-prod-01"
    assert results[0]["cve_id"] == "CVE-2024-5678"
    assert results[0]["exploit_status"] is True

def test_eol_adapter_parsing():
    raw_payload = json.dumps([
        {
            "asset_id": "EOL-SRV-9",
            "hostname": "db-legacy-01",
            "is_unsupported": True
        }
    ])

    results = EOLInventoryAdapter.parse_payload(raw_payload)

    assert len(results) == 1
    assert results[0]["external_id"] == "EOL-SRV-9"
    assert results[0]["asset_identifier"] == "db-legacy-01"
    assert results[0]["technical_severity"] == "High"