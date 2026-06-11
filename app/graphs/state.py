from typing import TypedDict

class AuditState(TypedDict):
    filename: str
    findings: list
    score: int
    risk_level: str
    explanation: str
    remediation: str
    report_path: str