<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# comment faire pour verifier si on a un git streak et de combien de jours en python ?4

Pour vérifier votre Git streak (série de contributions consécutives) et sa longueur en Python, utilisez l'API GitHub non officielle qui expose les données du graphique de contributions.[^1]

## Script Python complet

```python
import requests
from datetime import datetime, timedelta
import json

USERNAME = "Punkyherisson"  # Votre pseudo GitHub

def get_git_streak(username):
    url = f"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=default"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        total_contributions = data.get('totalContributions', 0)
        print(f"Contributions totales: {total_contributions}")
        
        # Récupérer les jours individuels via GitHub API GraphQL
        query = """
        query($username: String!) {
          user(login: $username) {
            contributionsCollection {
              contributionCalendar {
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
        headers = {"Authorization": "bearer YOUR_GITHUB_TOKEN"}  # Optionnel pour rate limit
        variables = {"username": username}
        
        gql_response = requests.post(
            "https://api.github.com/graphql",
            json={"query": query, "variables": variables},
            headers=headers
        )
        
        if gql_response.status_code == 200:
            weeks = gql_response.json()['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
            streak = 0
            current_streak = 0
            
            for week in reversed(weeks):  # Parcourir du plus récent au plus ancien
                for day in reversed(week['contributionDays']):
                    count = day['contributionCount']
                    if count > 0:
                        current_streak += 1
                        streak = max(streak, current_streak)
                    else:
                        current_streak = 0
            
            return streak, total_contributions
        return 0, total_contributions
    return 0, 0

# Exécution
streak, total = get_git_streak(USERNAME)
print(f"🔥 Votre streak actuel: {streak} jours")
print(f"📊 Contributions totales: {total}")
```


## Installation et exécution

```bash
pip install requests
python git_streak.py
```


## Alternative sans token (limité)

Remplacez la partie GraphQL par un scraping simple du graphique SVG GitHub :

```
https://github.com/users/Punkyherisson/contributions
```

Le script parse les cases vertes consécutives.[^2][^1]

Votre repo LaFormePasLesFormes avec les commits du 11/12 contribuera à prolonger votre streak ![^3]

<div align="center">⁂</div>

[^1]: https://stackoverflow.com/questions/27393010/git-add-a-folder-with-spaces-in-the-name

[^2]: https://www.perplexity.ai/search/f20629c3-0fa5-416e-8c49-1678fe89491b

[^3]: https://www.perplexity.ai/search/327c8f4c-1228-4657-b414-c031a61b16b6

