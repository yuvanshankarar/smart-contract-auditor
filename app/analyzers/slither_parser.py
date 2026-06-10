import json


def parse_slither_output(raw_json):

    data = json.loads(raw_json)

    findings = []

    detectors = data.get("results", {}).get("detectors", [])

    for detector in detectors:

        findings.append({
            "check": detector.get("check"),
            "severity": detector.get("impact"),
            "confidence": detector.get("confidence"),
            "description": detector.get("description")
        })

    return findings