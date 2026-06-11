import json


def parse_slither_output(raw_data):

    if isinstance(raw_data, str):
        data = json.loads(raw_data)
    else:
        data = raw_data

    findings = []

    detectors = data.get(
        "results",
        {}
    ).get(
        "detectors",
        []
    )

    for detector in detectors:

        findings.append({
            "check": detector.get("check"),
            "severity": detector.get("impact"),
            "confidence": detector.get("confidence"),
            "description": detector.get("description")
        })

    return findings