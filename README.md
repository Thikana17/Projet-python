# Mini API Python

[![CI](https://github.com/Thikana17/Projet-python/actions/workflows/ci.yml/badge.svg)](https://github.com/Thikana17/Projet-python/actions/workflows/ci.yml)

Une API REST modulaire et testée construite avec FastAPI offrant un ensemble d'outils mathématiques, de traitement de texte, de conversion et de validation de données.

---

## Sommaire
- [Installation](#1-installation)
- [Lancement](#2-lancement)
- [Utilisation & Endpoints](#3-utilisation--endpoints)
- [Tests et Qualité](#4-tests-et-qualité)
- [Contribuer](#5-contribuer)
- [Équipe](#6-équipe)
- [Licence](#licence)

---

## 1. Installation

### Prérequis
- Python 3.12+ (ou supérieur)
- Git

### Cloner le dépôt et installer les dépendances
```bash
git clone https://github.com/Thikana17/Projet-python.git
cd Projet-python
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 2. Lancement

### En local avec Uvicorn
```bash
uvicorn app.main:app --reload
```
L'API est accessible sur `http://localhost:8000`.  
La documentation interactive Swagger est disponible sur `http://localhost:8000/docs`.

### Avec Docker
```bash
# Construction de l'image
docker build -t mini-api .

# Exécution du conteneur
docker run -p 8000:8000 mini-api
```

---

## 3. Utilisation & Endpoints

### Santé de l'API
```bash
curl http://localhost:8000/sante
# Réponse: {"statut": "API active"}
```

### Module Validation
- **Validation d'adresse e-mail :**
  ```bash
  curl http://localhost:8000/validation/email/contact@exemple.fr
  # Réponse 200: {"email": "contact@exemple.fr", "valide": true}
  ```
- **Validation de robustesse de mot de passe :**
  ```bash
  curl http://localhost:8000/validation/mdp/Secr3t!Pass
  # Réponse 200: {"mdp": "Secr3t!Pass", "valide": true}
  ```
- **Validation de code postal :**
  ```bash
  curl http://localhost:8000/validation/code-postal/75001
  # Réponse 200: {"cp": "75001", "valide": true}
  ```

### Module Mathématiques
- **Factorielle :**
  ```bash
  curl http://localhost:8000/factorielle/5
  # Réponse 200: {"n": 5, "resultat": 120}
  ```

---

## 4. Tests et Qualité

### Lancer les tests unitaires et d'intégration
```bash
pytest -v
```

### Vérifier la couverture de code (seuil minimal 80 %)
```bash
pytest -v --cov=app --cov-fail-under=80
```

### Linter et formateur avec Ruff
```bash
ruff check .
```

---

## 5. Contribuer

Le projet applique la stratégie **GitHub Flow** :
1. Partir d'une branche `main` à jour :
   ```bash
   git switch main
   git pull origin main
   ```
2. Créer une branche dédiée nommée selon la convention `type/numéro-description` :
   ```bash
   git switch -c feat/12-ma-fonctionnalite
   ```
3. Effectuer des **commits atomiques** au format [Conventional Commits](https://www.conventionalcommits.org/) :
   - `feat:` nouvelle fonctionnalité
   - `fix:` correction de bug
   - `test:` ajout ou modification de tests
   - `docs:` documentation
   - `chore:` maintenance et outillage
4. Pousser la branche et ouvrir une **Pull Request** vers `main`.
5. Obtenir au moins une relecture argumentée et l'approbation d'un pair avec des tests CI validés avant fusion.

---

## 6. Équipe

| Membre | Rôle & Modules pris en charge |
| :--- | :--- |
| **Justinbdna** | Module `validation` (`email_valide`, `mdp_robuste`, `code_postal`), tests d'API et documentation |
| **DaupinDavid** | Module `math` (`factorielle`, `est_premier`, `pgcd`), gestion des erreurs partagée `app/erreurs.py` |
| **Thikana17** | Module `conversion` (`celsius_fahrenheit`, `km_miles`, `euros_devise`) |
| **aboulfaidhafsa** | Module `texte` (`est_palindrome`, `compter_voyelles`, `inverser`) |

---

## Licence
Ce projet est distribué sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.