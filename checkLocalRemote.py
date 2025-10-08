import os
import csv

# Chemin vers ton dossier local contenant les projets clonés
local_path = r"C:\Github.com\Punkyherisson"
local_folders = [f for f in os.listdir(local_path) if os.path.isdir(os.path.join(local_path, f))]

# Récupération des noms de dépôts GitHub depuis ton CSV
with open("depots_github_complete.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    github_repos = [row["Nom"] for row in reader]

# Dépôts présents sur GitHub mais absents localement
missing_local = set(github_repos) - set(local_folders)
print("Dépôts présents sur GitHub mais non clonés localement :")
for repo in missing_local:
    print("-", repo)