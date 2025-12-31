import os
from dotenv import load_dotenv
import requests
from datetime import date

load_dotenv()

USERNAME = "Punkyherisson"
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ TOKEN manquant ! Créez .env avec :")
    print("TOKEN=ghp_votre_token")
    print("USERNAME=Punkyherisson")
    exit()

def get_git_streak(username, token):
    url = "https://api.github.com/graphql"
    query = """
    query($username: String!) {
      user(login: $username) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """
    headers = {"Authorization": f"Bearer {token}"}
    variables = {"username": username}

    r = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
    r.raise_for_status()
    data = r.json()

    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    total = calendar["totalContributions"]

    # Aplatir tous les jours
    days = []
    for week in weeks:
        for d in week["contributionDays"]:
            days.append({
                "date": date.fromisoformat(d["date"]),
                "count": d["contributionCount"],
            })
    days.sort(key=lambda x: x["date"])

    # Streak actuel (depuis la fin)
    longest_streak = 0
    current_streak = 0
    last_idx = None
    for i in range(len(days) - 1, -1, -1):
        if days[i]["count"] > 0:
            last_idx = i
            break

    if last_idx is not None:
        current_streak = 1
        for i in range(last_idx, 0, -1):
            if days[i]["count"] > 0 and (days[i]["date"] - days[i - 1]["date"]).days == 1:
                current_streak += 1
            else:
                break

    # Plus long streak historique
    tmp_streak = 0
    for i, d in enumerate(days):
        if d["count"] > 0:
            if i > 0 and (d["date"] - days[i - 1]["date"]).days == 1:
                tmp_streak += 1
            else:
                tmp_streak = 1
            if tmp_streak > longest_streak:
                longest_streak = tmp_streak
        else:
            tmp_streak = 0

    return current_streak, longest_streak, total

if __name__ == "__main__":
    streak_actuel, streak_max, total = get_git_streak(USERNAME, TOKEN)
    print(f"Streak actuel : {streak_actuel} jours")
    print(f"Streak max    : {streak_max} jours")
    print(f"Contributions sur l'année : {total}")