def explain_vulnerability(finding):

   return """
Risk Explanation:
This contract contains a potential reentrancy vulnerability.

Attack Scenario:
An attacker can repeatedly call the vulnerable withdrawal function before the contract updates its internal balance records.

Impact:
The attacker may be able to withdraw funds multiple times, leading to financial loss and corruption of contract state.
"""