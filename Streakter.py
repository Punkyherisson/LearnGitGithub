import requests
from datetime import date

USERNAME = "Punkyherisson"
TOKEN = ""

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
    headers = {"Authorization": f"bearer {token}"}
    variables = {"username": username}

    r = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
    r.raise_for_status()
    data = r.json()

    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    total = calendar["totalContributions"]

    # Aplatir tous les jours dans une seule liste triée par date croissante
    days = []
    for week in weeks:
        for d in week["contributionDays"]:
            days.append({
                "date": date.fromisoformat(d["date"]),
                "count": d["contributionCount"],
            })
    days.sort(key=lambda x: x["date"])

    # Streak max (historiquement) et streak actuel
    longest_streak = 0
    current_streak = 0

    # Pour le streak actuel, on va partir de la fin (jour le plus récent)
    # et remonter tant qu'il y a des contributions sur les jours consécutifs.
    # Si aujourd'hui n'a pas encore de contributions, on commence au dernier
    # jour avec une contribution > 0.
    today = date.today()

    # trouver l'index du dernier jour avec une contribution > 0
    last_idx = None
    for i in range(len(days) - 1, -1, -1):
        if days[i]["count"] > 0:
            last_idx = i
            break

    if last_idx is not None:
        current_streak = 1
        # remonter tant que les jours sont consécutifs et count > 0
        for i in range(last_idx, 0, -1):
            if days[i]["count"] > 0 and (days[i]["date"] - days[i - 1]["date"]).days == 1:
                current_streak += 1
            else:
                break
    else:
        current_streak = 0

    # Calcul du plus long streak (toute la période)
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
