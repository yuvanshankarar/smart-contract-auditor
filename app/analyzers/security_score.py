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

        severity = (
            finding.get("severity", "")
            .lower()
        )

        if severity == "high":
            score -= 30

        elif severity == "medium":
            score -= 15

        elif severity == "low":
            score -= 5

        elif severity == "informational":
            score -= 1

    return max(score, 0)


def get_risk_level(score):

    if score >= 80:
        return "Low"

    elif score >= 60:
        return "Medium"

    else:
        return "High"