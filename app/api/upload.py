from fastapi import APIRouter, UploadFile, File, HTTPException
import os

router = APIRouter()

UPLOAD_DIR = "contracts"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-contract")
async def upload_contract(file: UploadFile = File(...)):

    if not file.filename.endswith(".sol"):
        raise HTTPException(
            status_code=400,
            detail="Only Solidity (.sol) files allowed"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "status": "uploaded",
        "path": file_path
    }