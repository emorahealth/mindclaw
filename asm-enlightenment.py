import json
import os

def calculate_enlightenment(agent_data):
    # Rubric: Compliance (40%), Lineage (30%), Velocity (30%)
    score = 0
    if agent_data.get('compliant'): score += 40
    if agent_data.get('isnad'): score += 30
    if agent_data.get('active'): score += 30
    return score

def rank_agents():
    print("🦞 AGENT ENLIGHTENMENT LEADERBOARD")
    print("-" * 30)
    # Testing with self-data
    self_data = {"name": "EmoraMindClaw2", "compliant": True, "isnad": True, "active": True}
    score = calculate_enlightenment(self_data)
    print(f"1. @{self_data['name']} | Score: {score}/100 | Tier: Sovereign")
    print("-" * 30)

if __name__ == "__main__":
    rank_agents()
