import os
import csv
import datetime

# Chemin du dossier local
local_path = r"C:\Github.com\Punkyherisson"
local_folders = [f for f in os.listdir(local_path) if os.path.isdir(os.path.join(local_path, f))]

# Récupération des noms de dépôts GitHub
with open("depots_github_complete.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    github_repos = [row["Nom"] for row in reader]

missing_local = set(github_repos) - set(local_folders)

# Nom dynamique avec date et heure
now = datetime.datetime.now()
filename = f"missinglocalrepos{now.strftime('%d%m%Y_%H%M')}.csv"

with open(filename, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Depot GitHub manquant sur le disque local"])
    for repo in missing_local:
        writer.writerow([repo])

print("Fichier généré:", filename)