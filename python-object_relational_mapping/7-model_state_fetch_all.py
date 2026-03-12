#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # 1. Création du moteur (le tunnel vers la base)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # 2. Création de la Session (l'interface de travail)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. La Requête (Purement Python !)
    # On demande à la session d'interroger le modèle State
    states = session.query(State).order_by(State.id).all()

    # 4. Affichage
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 5. Fermeture
    session.close()
