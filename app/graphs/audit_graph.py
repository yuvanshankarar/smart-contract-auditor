from langgraph.graph import StateGraph, END

from app.graphs.state import AuditState
from app.services.ai_explainer import explain_vulnerability
from app.reports.pdf_generator import generate_report
from app.storage.last_scan import LAST_SCAN


def scan_node(state: AuditState):
    print("Running Scan Agent")

    # Use real scan if available
    if LAST_SCAN:
        state["findings"] = LAST_SCAN.get("findings", [])
        state["score"] = LAST_SCAN.get("score", 0)
        state["risk_level"] = LAST_SCAN.get(
            "risk_level",
            "Unknown"
        )
    else:
        # Fallback test data
        state["findings"] = [
            {
                "check": "reentrancy-eth",
                "severity": "High",
                "description": "Reentrancy vulnerability detected."
            }
        ]

        state["score"] = 78
        state["risk_level"] = "Medium"

    return state


def explanation_node(state: AuditState):
    print("Running Explanation Agent")

    if state["findings"]:
        try:
            state["explanation"] = explain_vulnerability(
    state["findings"][0]["description"]
)
        except Exception as e:
            state["explanation"] = (
                f"AI explanation failed: {e}"
            )

    return state


def remediation_node(state: AuditState):
    print("Running Remediation Agent")

    state["remediation"] = (
        "Use the Checks-Effects-Interactions pattern and "
        "OpenZeppelin ReentrancyGuard."
    )

    return state


def pdf_node(state: AuditState):
    print("Running PDF Agent")

    pdf_path = generate_report(
    filename=state["filename"],
    score=state["score"],
    risk_level=state["risk_level"],
    findings=state["findings"],
    explanation=state["explanation"],
    remediation=state["remediation"]
)

    state["report_path"] = pdf_path

    return state


builder = StateGraph(AuditState)

builder.add_node("scan", scan_node)
builder.add_node("explain", explanation_node)
builder.add_node("remediate", remediation_node)
builder.add_node("pdf", pdf_node)

builder.set_entry_point("scan")

builder.add_edge("scan", "explain")
builder.add_edge("explain", "remediate")
builder.add_edge("remediate", "pdf")
builder.add_edge("pdf", END)

graph = builder.compile()