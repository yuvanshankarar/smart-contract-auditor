from fastapi import APIRouter

from app.schemas.explain import ExplainRequest
from app.agents.explainer_agent import explain_vulnerability

router = APIRouter()

@router.post("/explain")
def explain(request: ExplainRequest):

    explanation = explain_vulnerability(
        request.vulnerability
    )

    return {
        "explanation": explanation
    }