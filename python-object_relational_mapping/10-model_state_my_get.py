#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # 1. Tentative de connexion
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 2. On récupère l'argument
    search_name = sys.argv[4]

    # 3. La requête
    state = session.query(State).filter(State.name == search_name).first()

    # 4. L'affichage (C'est ici que ça doit parler !)
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
