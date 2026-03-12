#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion au moteur
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. On cherche tous les états qui contiennent 'a'
    states_to_delete = session.query(State).filter(
        State.name.contains('a')
    ).all()

    # 2. On les supprime un par un de la session
    for state in states_to_delete:
        session.delete(state)

    # 3. On valide définitivement la suppression
    session.commit()

    session.close()
