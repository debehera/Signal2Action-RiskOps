from src.core.normalizer import FindingNormalizer

def test_normalize_scanner_finding():
    sample_parsed = {
        "source": "vulnerability_scanner",
        "external_id": "VULN-001",
        "asset_identifier": "srv-sql-01.corp",
        "cve_id": "CVE-2023-1234",
        "technical_severity": "Critical",
        "exploit_status": True,
        "raw_payload": {"cve": "CVE-2023-1234", "severity": "Critical"}
    }

    normalized = FindingNormalizer.normalize(sample_parsed)

    assert normalized["source"] == "vulnerability_scanner"
    assert normalized["asset_identifier"] == "srv-sql-01.corp"
    assert normalized["technical_severity"] == "Critical"
    assert normalized["severity_score"] == 4
    assert normalized["exploit_status"] is True
    assert normalized["status"] == "OPEN"

def test_normalize_eol_finding():
    sample_parsed = {
        "source": "eol_inventory",
        "external_id": "EOL-88",
        "asset_identifier": "192.168.1.50",
        "cve_id": "EOL-RISK",
        "technical_severity": "High",
        "exploit_status": False,
        "raw_payload": {"hostname": "192.168.1.50", "is_unsupported": True}
    }

    normalized = FindingNormalizer.normalize(sample_parsed)

    assert normalized["source"] == "eol_inventory"
    assert normalized["technical_severity"] == "High"
    assert normalized["severity_score"] == 3
    assert normalized["exploit_status"] is False