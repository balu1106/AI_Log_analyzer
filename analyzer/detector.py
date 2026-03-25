import re

patterns = {
    "email": r"\S+@\S+",
    "password": r"password\s*=\s*\S+",
    "api_key": r"sk-\w+",
    "phone": r"\b\d{10}\b"
}

risk_map = {
    "email": "low",
    "password": "critical",
    "api_key": "high",
    "phone": "low",
    "error": "medium"
}

def detect(lines):
    findings = []

    for i, line in enumerate(lines):
        for key, pattern in patterns.items():
            if re.search(pattern, line):
                findings.append({
                    "type": key,
                    "risk": risk_map[key],
                    "line": i + 1
                })

        # Detect errors / stack traces
        if "error" in line.lower() or "exception" in line.lower():
            findings.append({
                "type": "error",
                "risk": "medium",
                "line": i + 1
            })

    return findings