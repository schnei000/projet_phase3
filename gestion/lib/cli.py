from datetime import date
from .models import Session, Utilisateur, Categorie, Depense

session = Session()

#creation du menu
Menu_choix = {
    "1": "Ajouter utilisateur",
    "2": "Ajouter catégorie",
    "3": "Ajouter dépense",
    "4": "Voir les dépenses",
    "5": "Voir tous les utilisateurs",
    "6": "Voir toutes les catégories",
    "7": "Statistiques",
    "0": "Quitter"
}


def input_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def input_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Veuillez entrer un nombre flottant valide.")

# Fonction CRUD
def ajouter_utilisateur(session):
    nom = input("Nom de l'utilisateur : ").strip()
    if not nom:
        print("Nom invalide.")
        return
    session.add(Utilisateur(nom=nom))
    session.commit()
    print(f"Utilisateur {nom} ajouté.")

def ajouter_categorie(session):
    nom = input("Nom de la catégorie : ").strip()
    if not nom:
        print("Nom invalide.")
        return
    session.add(Categorie(nom=nom))
    session.commit()
    print(f"Catégorie {nom} ajoutée.")

def ajouter_depense(session):
    description = input("Description de la dépense : ").strip()
    montant = input_float("Montant : ")
    date_str = input("Date (YYYY-MM-DD, Entrée = aujourd'hui) : ").strip()
    if not date_str:
        date_str = str(date.today())

    utilisateur_id = input_int("ID utilisateur : ")
    categorie_id = input_int("ID catégorie : ")

    session.add(Depense(
        description=description,
        montant=montant,
        date=date_str,
        utilisateur_id=utilisateur_id,
        categorie_id=categorie_id
    ))
    session.commit()
    print(f"Dépense '{description}' ajoutée.")

def voir_depenses(session):
    depenses = session.query(Depense).all()
    if not depenses:
        print("Aucune dépense.")
        return
    for d in depenses:
        print(f"ID:{d.id}  {d.description}  {d.montant:.2f} $  {d.date}  "
              f"user:{d.utilisateur_id}  cat:{d.categorie_id}")

def voir_utilisateurs(session):
    users = session.query(Utilisateur).all()
    if not users:
        print("Aucun utilisateur.")
        return
    for u in users:
        print(f"ID:{u.id}  Nom:{u.nom}")

def voir_categories(session):
    cats = session.query(Categorie).all()
    if not cats:
        print("Aucune catégorie.")
        return
    for c in cats:
        print(f"ID:{c.id}  Nom:{c.nom}")

def statistiques(session):
    depenses = session.query(Depense).all()
    total = sum(d.montant for d in depenses) if depenses else 0.0
    print(f"Nombre de dépenses : {len(depenses)}")
    print(f"Total des dépenses : {total:.2f} $")
    return len(depenses), total


def main():
    while True:
        print("\nMenu")
        for k, v in Menu_choix.items():
            print(f"{k}: {v}")
        choix = input("Entrez votre choix : ").strip()

        if choix == "1":
            ajouter_utilisateur(session)
        elif choix == "2":
            ajouter_categorie(session)
        elif choix == "3":
            ajouter_depense(session)
        elif choix == "4":
            voir_depenses(session)
        elif choix == "5":
            voir_utilisateurs(session)
        elif choix == "6":
            voir_categories(session)
        elif choix == "7":
            statistiques(session)
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")
    session.close()