import requests

USERNAME = "Punkyherisson"  # ton pseudo GitHub
TOKEN = ""  # token perso (classic ou fine-grained) avec scope minimal "read:user"

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

    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    total = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

    current_streak = 0
    longest_streak = 0

    # on parcourt les jours du plus récent au plus ancien
    for week in reversed(weeks):
        for day in reversed(week["contributionDays"]):
            if day["contributionCount"] > 0:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                # si tu veux le *streak actuel*, on casse à la première journée à 0
                break
        else:
            # continue si la boucle interne n'a pas été cassée
            continue
        break

    return current_streak, longest_streak, total

if __name__ == "__main__":
    streak_actuel, streak_max, total = get_git_streak(USERNAME, TOKEN)
    print(f"Streak actuel : {streak_actuel} jours")
    print(f"Streak max    : {streak_max} jours")
    print(f"Contributions sur l'année : {total}")
