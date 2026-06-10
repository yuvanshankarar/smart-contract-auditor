def explain_vulnerability(finding):

    return f"""
Risk Explanation:
{finding}

Attack Scenario:
An attacker repeatedly invokes a vulnerable function before state updates occur.

Impact:
Funds may be drained and contract state corrupted.
"""