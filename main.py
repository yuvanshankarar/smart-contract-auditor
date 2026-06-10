from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.analyze import router as analyze_router
from app.api.scan import router as scan_router
from app.api.explain import router as explain_router
from app.api.report import router as report_router

app = FastAPI(
    title="AI Smart Contract Auditor"
)

app.include_router(upload_router)
app.include_router(analyze_router)
app.include_router(scan_router)
app.include_router(explain_router)
app.include_router(report_router)

@app.get("/")
def root():
    return {
        "message": "Smart Contract Auditor Running"
    }