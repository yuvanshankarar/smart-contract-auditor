import re

def analyze_contract(code: str):

    findings = []

    if ".call{" in code:
        findings.append({
            "type": "Potential Reentrancy",
            "severity": "Critical",
            "description": "Low-level call detected."
        })

    if "tx.origin" in code:
        findings.append({
            "type": "tx.origin Usage",
            "severity": "High",
            "description": "Authentication via tx.origin is unsafe."
        })

    if "selfdestruct" in code:
        findings.append({
            "type": "Selfdestruct Usage",
            "severity": "Medium",
            "description": "Contract can be destroyed."
        })

    return findings