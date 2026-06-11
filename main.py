from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.analyze import router as analyze_router
from app.api.scan import router as scan_router
from app.api.explain import router as explain_router
from app.api.report import router as report_router
from app.api.history import router as history_router
from app.database import Base, engine
from app.models.scan import Scan

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="AI Smart Contract Auditor"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later change to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(upload_router)
app.include_router(analyze_router)
app.include_router(scan_router)
app.include_router(explain_router)
app.include_router(report_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message": "Smart Contract Auditor Running"
    }