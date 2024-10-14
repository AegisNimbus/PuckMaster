import json
import os

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f)

def update_leaderboard(player_name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"name": player_name, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    leaderboard = leaderboard[:10]  # Keep only top 10 scores
    save_leaderboard(leaderboard)

def get_leaderboard():
    return load_leaderboard()
