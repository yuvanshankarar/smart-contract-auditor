from fastapi import APIRouter, UploadFile, File

from app.analyzers.basic_analyzer import analyze_contract

router = APIRouter()


@router.post("/analyze-contract")
async def analyze(file: UploadFile = File(...)):

    content = await file.read()

    code = content.decode("utf-8")

    findings = analyze_contract(code)

    return {
        "filename": file.filename,
        "issues_found": len(findings),
        "findings": findings
    }