import json
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Dict, Any

from src.connectors.scanner_adapter import VulnerabilityScannerAdapter
from src.connectors.eol_adapter import EOLInventoryAdapter
from src.core.normalizer import FindingNormalizer

router = APIRouter()

class IngestRequest(BaseModel):
    source_type: str  # "scanner" or "eol"
    payload: List[Dict[str, Any]]

@router.post("/findings/ingest", status_code=status.HTTP_201_CREATED)
def ingest_findings(request: IngestRequest):
    """
    Ingests and normalizes raw findings from vulnerability scanners or EOL feeds.
    """
    raw_json_str = json.dumps(request.payload)

    if request.source_type == "scanner":
        parsed_records = VulnerabilityScannerAdapter.parse_payload(raw_json_str)
    elif request.source_type == "eol":
        parsed_records = EOLInventoryAdapter.parse_payload(raw_json_str)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported source_type: {request.source_type}. Use 'scanner' or 'eol'."
        )

    normalized_findings = [FindingNormalizer.normalize(record) for record in parsed_records]

    return {
        "status": "success",
        "ingested_count": len(normalized_findings),
        "source_type": request.source_type,
        "findings": normalized_findings
    }