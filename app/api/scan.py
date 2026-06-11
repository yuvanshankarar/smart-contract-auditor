import json

from app.database import SessionLocal
from app.models.scan import Scan
from fastapi import APIRouter, UploadFile, File
import os

from app.storage.last_scan import LAST_SCAN
from app.graphs.audit_graph import graph
from app.storage.scan_history import SCAN_HISTORY

from app.analyzers.slither_analyzer import run_slither
from app.analyzers.slither_parser import parse_slither_output
from app.analyzers.security_score import (
    calculate_score,
    get_risk_level
)

router = APIRouter()

UPLOAD_DIR = "contracts"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/scan-contract")
async def scan_contract(
    file: UploadFile = File(...)
):

    if not file.filename:
        return {
            "error": "Filename is required"
        }

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    # Temporary hardcoded findings
    report = run_slither(file_path)
    findings = parse_slither_output(report)

    findings = [
        {
            "check": "reentrancy-eth",
            "severity": "High",
            "description": "Reentrancy vulnerability detected."
        }
    ]

    score = calculate_score(findings)

    risk_level = get_risk_level(score)

    result = graph.invoke({
        "filename": file_path,
        "findings": findings,
        "score": score,
        "risk_level": risk_level,
        "explanation": "",
        "remediation": "",
        "report_path": ""
    })

    LAST_SCAN.clear()

    LAST_SCAN.update(result)

    db = SessionLocal()

    db_scan = Scan(
        filename=result["filename"],
        score=result["score"],
        risk_level=result["risk_level"],
        findings=json.dumps(result["findings"]),
        explanation=result["explanation"],
        remediation=result["remediation"],
        report_path=result["report_path"]
   )

    print("Saving scan to database...")
    print("Filename:", result["filename"])
    print("Score:", result["score"])

    db.add(db_scan)

    try:
        db.commit()
        print("Scan saved successfully!")
    except Exception as e:
        print("DATABASE ERROR:", e)
        db.rollback()

    db.close()

    return {
        "filename": result["filename"],
        "security_score": result["score"],
        "risk_level": result["risk_level"],
        "issues_found": len(result["findings"]),
        "findings": result["findings"],
        "explanation": result["explanation"],
        "remediation": result["remediation"],
        "report_path": result["report_path"]
    }