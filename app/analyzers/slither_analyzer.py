def run_slither(contract_path):
    """
    Temporary mock Slither output.

    Replace with real Slither integration later.
    """

    print("Mock Slither Scan Running")
    print("Contract:", contract_path)

    return {
        "results": {
            "detectors": [
                {
                    "check": "reentrancy-eth",
                    "impact": "High",
                    "confidence": "High",
                    "description": "Reentrancy vulnerability detected."
                }
            ]
        }
    }