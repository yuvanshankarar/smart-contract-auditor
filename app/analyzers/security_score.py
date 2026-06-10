SEVERITY_WEIGHTS = {
    "Critical": 30,
    "High": 20,
    "Medium": 10,
    "Low": 5,
    "Informational": 1
}


def calculate_score(findings):

    score = 100

    for finding in findings:

        severity = finding.get("severity", "Informational")

        score -= SEVERITY_WEIGHTS.get(
            severity,
            0
        )

    return max(score, 0)


def get_risk_level(score):

    if score >= 90:
        return "Low"

    elif score >= 70:
        return "Medium"

    elif score >= 50:
        return "High"

    return "Critical"