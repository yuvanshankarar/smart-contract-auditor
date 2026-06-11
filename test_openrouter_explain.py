from app.services.ai_explainer import explain_vulnerability

print(
    explain_vulnerability(
        "Reentrancy vulnerability detected."
    )
)