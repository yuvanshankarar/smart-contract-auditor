from app.reports.pdf_generator import generate_report

findings = [
    {
        "check": "reentrancy-eth",
        "severity": "High",
        "description": "Reentrancy vulnerability detected."
    }
]

path = generate_report(
    filename="reentrancy.sol",
    score=78,
    risk_level="Medium",
    findings=findings
)

print(path)