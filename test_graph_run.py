from app.graphs.audit_graph import graph

result = graph.invoke({
    "filename": r"C:\Users\artwi\Desktop\Smart Contract Auditor\contracts\reentrancy.sol",
    "findings": [],
    "score": 0,
    "risk_level": "",
    "explanation": "",
    "remediation": "",
    "report_path": ""
})

print(result)