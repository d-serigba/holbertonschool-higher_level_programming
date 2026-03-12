#!/usr/bin/python3
"""
Contains the class definition of a State and
an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# L'instance Base est la fondation (le chassis) de tous nos futurs modèles
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base and links to the MySQL table states.
    """
    __tablename__ = 'states'

    # Colonne ID : clé primaire, auto-générée, entier unique
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Colonne Name : chaîne de 128 caractères max, ne peut pas être nulle
    name = Column(String(128), nullable=False)
