<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Je voudrais faire un tableau excel avec tous les depots que j'ai ici :

[Your Repositories](https://github.com/Punkyherisson?tab=repositories)

Voici comment obtenir et organiser dans Excel la liste complète des dépôts publics GitHub d’un utilisateur : il faut utiliser l’API GitHub ou des méthodes Python automatisées, car il n’existe pas d’export direct sur le site web.[^1][^2][^3]

### Méthode rapide avec Python et l’API GitHub

- Installe la bibliothèque Requests : `pip install requests`.[^2]
- Utilise ton nom d’utilisateur (ici `Punkyherisson`) dans l’URL de l’API GitHub pour récupérer tes dépôts.
- Automatiquement, tu peux extraire les informations souhaitées (nom, description, langue, etc.) sous forme de liste à coller dans Excel.[^4][^5][^3]

```python
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
```

Ce script crée un fichier CSV que tu peux ouvrir directement avec Excel, liste tous tes dépôts publics avec nom, description, langage principal et URL.[^3][^2]

### Méthodes alternatives

- Utiliser le GitHub CLI (`gh repo list Punkyherisson --limit 100`) puis copier/coller dans Excel.[^1]
- Scraper la page HTML de tes dépôts avec Python et la librairie BeautifulSoup, mais l’API est plus fiable.[^2][^4]


### Points clés :

- L’API GitHub permet une extraction structurée des dépôts d’un utilisateur et l’exporte simplement vers un fichier Excel ou CSV.[^5][^3][^2]
- Tu peux personnaliser les colonnes dans ton tableau selon les besoins (nom, description, stars, date…).[^2]
- Il ne faut pas être connecté, sauf pour les dépôts privés (nécessite un token GitHub).[^6]


### Ressources :

- Documentation officielle de l’API repos GitHub.[^5]
- Tutoriel pour la méthode Python sur BrightData et StackOverflow.[^7][^3][^2]

Ainsi, cette solution te permet de générer automatiquement le tableau Excel souhaité pour tous tes dépôts GitHub, facile à mettre à jour et à importer dans Excel.[^3][^2]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://cli.github.com/manual/gh_repo_list

[^2]: https://brightdata.com/blog/how-tos/how-to-scrape-github-repositories-in-python

[^3]: https://gist.github.com/nikhita/54108c8fabc1ec79094410d07495f2e9

[^4]: https://arxiv.org/pdf/2012.03453.pdf

[^5]: https://docs.github.com/en/rest/repos

[^6]: https://airbyte.com/how-to-sync/how-to-export-github-issues-to-excel

[^7]: https://stackoverflow.com/questions/74857059/how-do-i-programmatically-extract-github-repositories-that-contain-a-code-string

[^8]: https://github.com/orgs/github/repositories

[^9]: https://github.com/trending

[^10]: https://www.hostinger.com/in/tutorials/most-popular-github-repos

[^11]: https://github.blog/news-insights/repository-search-on-all-repositories/

[^12]: https://github.com/orgs/community/discussions/24514

[^13]: https://stackoverflow.com/questions/41369365/how-can-i-export-github-issues-to-excel

[^14]: https://stackoverflow.com/questions/60368063/how-to-retrieve-the-list-of-all-pinned-github-repositories-of-a-person

[^15]: https://www.youtube.com/watch?v=Dz3CQHnNw_s

[^16]: https://github.com/topics/top-repos-list

[^17]: https://github.com/orgs/community/discussions/42844

[^18]: https://www.youtube.com/watch?v=cgOPg5cCr2g

[^19]: http://garyjackson.dev/posts/extract-github-repository-details/

[^20]: https://github.com/orgs/community/discussions/24634

