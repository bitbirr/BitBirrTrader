
def run_risk_analysis(token_address):
    if not token_address or len(token_address) < 32:
        return "High Risk: Invalid token address length."
    if token_address.startswith("9") or token_address.startswith("1"):
        return "No obvious red flags."
    return "Moderate Risk: Unknown prefix. Proceed cautiously."
