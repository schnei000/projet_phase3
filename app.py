from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

Engine = create_engine('sqlite:///Gestion.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=Engine)


class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)

class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    nom = Column(String)

class Depense(Base):
    __tablename__ = 'depenses'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    montant = Column(Float)
    date = Column(String, default=str(date.today()))
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    categorie_id = Column(Integer, ForeignKey('categories.id'))


Base.metadata.create_all(Engine)

# Creons une Menu
Menu_choix: dict[str, str] = {
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

# --- Fonctions CRUD ---
def ajouter_utilisateur(session):
    nom = input("Veuillez entrer le nom de l'utilisateur : ")
    if not nom:
        print("Nom invalide.")
        return
    new_utilisateur = Utilisateur(nom=nom)
    session.add(new_utilisateur)
    session.commit()
    print(f"L'utilisateur {nom} a été ajouté.")

def ajouter_categorie(session):
    nom = input("Veuillez entrer le nom de la catégorie : ")
    if not nom:
        print("Nom invalide.")
        return
    new_categorie = Categorie(nom=nom)
    session.add(new_categorie)
    session.commit()
    print(f"La catégorie {nom} a été ajoutée.")

def ajouter_depense(session):
    description = input("Veuillez entrer la description de la dépense : ")
    montant = input_float("veuillez entrer le montant de la dépense : ") 
    date = input("Veuillez entrer la date de la dépense (YYYY-MM-DD) ou appuyez sur Entrée pour aujourd'hui : ")
    utilisateur_id = input_int("Veuillez entrer l'ID de l'utilisateur : ")
    categorie_id = input_int("Veuillez entrer l'ID de la catégorie : ")

    new_depense = Depense(description=description, montant=montant, utilisateur_id=utilisateur_id, categorie_id=categorie_id)
    session.add(new_depense)
    session.commit()
    print(f"la Depense '{description}' a ete ajouter avec succes.")

def voir_depenses(session):
    depenses=session.query(Depense).all()
    if not depenses:
        print("Aucune dépense trouvée.")
        return
    for depense in depenses :
        print(f"ID: {depense.id}, Description: {depense.description}, Montant: {depense.montant}, Date: {depense.date}, Utilisateur ID: {depense.utilisateur_id}, Catégorie ID: {depense.categorie_id}")

def voir_utilisateurs(session):
    utilisateurs = session.query(Utilisateur).all()
    if not utilisateurs:
        print('Aucun utilisateur trouver')
        return
    for utilisateur in utilisateurs:
        print(f"ID:{utilisateur.id}, Nom: {utilisateur.nom}")

def voir_categories(session):
    categories = session.query(Categorie).all()
    if not categories:
        print('aucun Categorie trouver')
    for categori in categories:
        print(f'ID: {categori.id},Nom: {categori.nom}')

def statistiques(session):
    depenses = session.query(Depense).all()
    total = sum(depense.montant for depense in depenses)
    print(f'Nombre de depenses : {len(depenses)}')
    print(f'Total des depenses : {total:.2f}Dollar')

def main():
    session = Session()
    while True:
        print('Menu')
        for k,v in Menu_choix.items():
            print(f'{k}: {v}')
        choix = input('entrer votre choix:')

        if choix == '1':
          ajouter_utilisateur(session)
        elif choix =='2':
          ajouter_categorie(session)
        elif choix == '3':
            ajouter_depense(session)
        elif choix == '4':
            voir_depenses(session)
        elif choix == '5':
            voir_utilisateurs(session)
        elif choix == '6':
            voir_categories(session)
        elif choix == '7':
            statistiques(session)
        elif choix == '0':
            print('Au revoir')
            break
        else:
            print('mauvais choix ,reessayez')
    session.close()

if __name__== '__main__':
    main()
