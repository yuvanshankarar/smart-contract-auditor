from fastapi import APIRouter

from app.database import SessionLocal
from app.models.scan import Scan

router = APIRouter()


@router.get("/history")
def get_history():

    db = SessionLocal()

    scans = db.query(Scan).all()

    results = []

    for scan in scans:

        results.append({
            "id": scan.id,
            "filename": scan.filename,
            "score": scan.score,
            "risk_level": scan.risk_level,
            "report_path": scan.report_path
        })

    db.close()

    return results