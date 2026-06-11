from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.storage.last_scan import LAST_SCAN

router = APIRouter()


@router.get("/download-report")
def download_report():

    pdf_path = LAST_SCAN.get("report_path")

    if not pdf_path:
        return {
            "error": "No report generated yet"
        }

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="audit_report.pdf"
    )