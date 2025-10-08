import requests
import csv

username = "Punkyherisson"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
data = response.json()

with open("depots_github_complete.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Description", "Langage", "URL", "Readme Présent", "Dernière mise à jour"])
    for repo in data:
        # Check for README
        readme_url = f"https://api.github.com/repos/{username}/{repo['name']}/contents/README.md"
        readme_response = requests.get(readme_url)
        has_readme = "Oui" if readme_response.status_code == 200 else "Non"
        # Get last update date
        last_update = repo["updated_at"][:10] if "updated_at" in repo else ""
        writer.writerow([
            repo["name"],
            repo["description"] or "",
            repo["language"] or "",
            repo["html_url"],
            has_readme,
            last_update
        ])
