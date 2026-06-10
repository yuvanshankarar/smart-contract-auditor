from app.agents.remediation_agent import generate_fix

result = generate_fix(
    "reentrancy-eth"
)

print(result)