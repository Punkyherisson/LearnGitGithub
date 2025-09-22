import requests
import csv

username = "Punkyherisson"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
data = response.json()

with open("depots_github.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Description", "Langage", "URL"])
    for repo in data:
        writer.writerow([repo["name"], repo["description"], repo["language"], repo["html_url"]])