# LearnGitGithub 📚

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![GitHub Streak](https://github-readme-stats.vercel.app/api?username=Punkyherisson&show_icons=true&theme=radical&hide_border=true)](https://github.com/anuraghazra/github-readme-stats)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Repo Size](https://img.shields.io/github/repo-size/Punkyherisson/LearnGitGithub?color=orange)](https://github.com/Punkyherisson/LearnGitGithub)

Approfondir Git et GitHub à travers de petits exercices pratiques, des notes perso et des scripts utiles (**streak GitHub : 285 jours** 🥇).

---

## 🎯 Objectifs du dépôt

- Consolider les bases de Git (commit, branches, merge, rebase, etc.).
- Mieux comprendre le fonctionnement de GitHub (remote, issues, pull requests, etc.).
- Documenter une pratique quotidienne de Git.
- Expérimenter avec des scripts autour de l'API GitHub.

Ce dépôt sert de **bac à sable** pour progresser sur Git/GitHub au quotidien.

---

## 🧩 Contenu principal

### Streakter.py ⭐
Script Python qui interroge l'API GraphQL de GitHub pour afficher :
- le **streak actuel** (jours consécutifs avec contributions),
- le **streak maximal**,
- le **nombre total de contributions** sur l'année.

### Autres contenus
- Notes / exercices Git
- Commandes courantes
- Manipulation de branches
- Tests de workflows GitHub

---

## ⚙️ Utiliser le script Streakter.py

### Prérequis
```bash
pip install python-dotenv requests
```

### Configuration `.env`
```
TOKEN=ghp_votre_token_complet
USERNAME=Punkyherisson
```

### Lancer
```bash
python Streakter.py
```

**Exemple de sortie :**
```bash
Streak actuel : 285 jours
Streak max    : 284 jours  
Contributions sur l'année : 500
```

---

## 🔐 Sécurité

- **Token en `.env` uniquement** (jamais en clair dans le code).
- `.env` dans `.gitignore`.
- GitHub Push Protection activé ✅

---

## 📈 Mes stats GitHub

![Punkyherisson's GitHub stats](https://github-readme-stats.vercel.app/api?username=Punkyherisson&show_icons=true&theme=radical)

---

## 🧭 Prochaines étapes

- [ ] Workflows Git avancés (rebase interactif, cherry-pick)
- [ ] Scripts API GitHub (stats repos, issues, etc.)
- [ ] Tutoriels pas-à-pas en Markdown

---

## 📝 Licence

[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

**Auteur** : Punkyherisson  
**Streak actuel** : 285 jours 🥇