
# Gestionnaire de Budget – CLI + SQLAlchemy ORM

##  Description
Application en **ligne de commande (CLI)** développée en **Python** avec **SQLAlchemy ORM** pour gérer un petit budget personnel.  
Le projet permet d’enregistrer des utilisateurs, des catégories de dépenses, et des dépenses associées dans une base de données **SQLite**.

---

##  Fonctionnalités
1. Ajouter un utilisateur  
2. Ajouter une catégorie  
3. Ajouter une dépense  
4. Voir toutes les dépenses  
5. Voir tous les utilisateurs  
6. Voir toutes les catégories  
7. Afficher les statistiques (nombre et montant total des dépenses)

---

##  Structure du projet
projet_phase3/
├── .venv/                 
├── lib/
│   ├── init.py
│   ├── models.py         
│   └── cli.py             
├── .gitignore             
├── Gestion.db             
└── README.md  

---

## 🧪 Technologies utilisées
- **Python 3.8+**
- **SQLAlchemy** (ORM)
- **SQLite** (base de données locale)
- **venv** (gestion d’environnement virtuel)

---

##  Installation
```bash
# Cloner le dépôt
git clone https://github.com/schnei000/projet_phase3.git
cd projet_phase3

# Créer et activer l’environnement virtuel
python -m venv .venv
source .venv/bin/activate  

---

## Lancement
python app.py

---
Modèles de données
Utilisateur
id (int, PK)
nom (str)
Catégorie
id (int, PK)
nom (str)
Dépense
id (int, PK)
description (str)
montant (float)
date (str, format YYYY-MM-DD)
utilisateur_id (FK → Utilisateur)
categorie_id (FK → Categorie)
