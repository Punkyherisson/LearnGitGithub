import os
import csv
import datetime

# Chemin vers ton dossier local contenant les projets clonés
local_path = r"C:\Github.com\Punkyherisson"
local_folders = [f for f in os.listdir(local_path) if os.path.isdir(os.path.join(local_path, f))]

# Récupération des noms de dépôts GitHub depuis ton CSV
with open("depots_github_complete.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    github_repos = [row["Nom"] for row in reader]

# Dossiers présents localement mais absents sur GitHub
missing_github = set(local_folders) - set(github_repos)

# Génération du nom de fichier horodaté
now = datetime.datetime.now()
filename = f"missinggithubrepos{now.strftime('%d%m%Y_%H%M')}.csv"

# Écriture des dossiers locaux "orphelins" dans le fichier CSV
with open(filename, "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Dossier local absent de GitHub"])
    for repo in missing_github:
        writer.writerow([repo])

print(f"Fichier généré : {filename}")