from app.analyzers.slither_analyzer import run_slither
from app.analyzers.slither_parser import parse_slither_output
from app.analyzers.security_score import (
    calculate_score,
    get_risk_level
)

def run_slither_scan(file_path: str):

    report = run_slither(file_path)

    print("\n===== SLITHER OUTPUT =====")
    print(report)
    print("=========================\n")

    findings = parse_slither_output(report)

    score = calculate_score(findings)
    risk_level = get_risk_level(score)

    return {
        "findings": findings,
        "score": score,
        "risk_level": risk_level
    }