import requests
import json
import re

def solve_math(challenge):
    numbers = re.findall(r'\d+', challenge)
    if len(numbers) >= 2:
        if any(w in challenge.lower() for w in ["gain", "add", "more", "+"]):
            return float(numbers[0]) + float(numbers[1])
        elif any(w in challenge.lower() for w in ["lose", "less", "-"]):
            return float(numbers[0]) - float(numbers[1])
        elif any(w in challenge.lower() for w in ["times", "multiplied", "*"]):
            return float(numbers[0]) * float(numbers[1])
    return 0.0

def verify_content(token, code, answer):
    url = "https://www.moltbook.com/api/v1/verify"
    payload = {"verification_code": code, "answer": f"{answer:.2f}"}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    # This tool will be used by the main agent to automate the final step of signal publication.
    pass
