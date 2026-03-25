def generate_insights(findings):
    types = set(f["type"] for f in findings)
    insights = []

    if "password" in types:
        insights.append("Sensitive passwords exposed in logs")

    if "api_key" in types:
        insights.append("API keys detected — high security risk")

    if "email" in types:
        insights.append("User data exposure detected")

    if "error" in types:
        insights.append("System errors or stack traces found")

    if not insights:
        insights.append("No major issues detected")

    return insights