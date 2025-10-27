#  les modeles(Table) de notre application
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/Gestion.db", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    depenses = relationship("Depense", backref="utilisateur", cascade="all, delete-orphan")

class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    depenses = relationship("Depense", backref="categorie", cascade="all, delete-orphan")

class Depense(Base):
    __tablename__ = 'depenses'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    montant = Column(Float, nullable=False)
    date = Column(String, default=str(date.today()))
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'), nullable=False)
    categorie_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

def init_db():
    Base.metadata.create_all(engine)