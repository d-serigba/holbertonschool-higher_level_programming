#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Création du nouvel objet State
    new_state = State(name="Louisiana")

    # 2. Ajout à la session (Staging)
    session.add(new_state)

    # 3. Validation de la transaction (Commit)
    # C'est ici que MySQL génère l'ID
    session.commit()

    # 4. Affichage du nouvel ID
    print("{}".format(new_state.id))

    session.close()
