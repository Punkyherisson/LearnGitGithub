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