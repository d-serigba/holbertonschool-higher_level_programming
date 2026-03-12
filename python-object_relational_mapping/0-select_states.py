#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the database and prints all states sorted by id.
    """
    # Connexion à la base avec les arguments passés en ligne de commande
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création du curseur pour exécuter des requêtes
    cursor = db.cursor()

    # Exécution de la requête SQL demandée
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération de toutes les lignes
    rows = cursor.fetchall()

    # Affichage des résultats au format (id, 'name')
    for row in rows:
        print(row)

    # Fermeture propre des ressources
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
