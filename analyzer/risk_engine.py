def calculate_risk(findings):
    scores = {
        "critical": 5,
        "high": 3,
        "medium": 2,
        "low": 1
    }

    total = sum(scores[f["risk"]] for f in findings)

    if total >= 10:
        level = "high"
    elif total >= 5:
        level = "medium"
    else:
        level = "low"

    return total, level