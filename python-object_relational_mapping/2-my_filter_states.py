#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument provided by the user.
"""
import MySQLdb
import sys


def filter_by_user_input():
    """
    Connects to the database and filters states by the exact name
    passed as the 4th argument.
    """
    # Récupération des 4 arguments nécessaires
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion au serveur MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    # Création de la requête en utilisant .format()
    # Utilisation d'une seule ligne ou parenthèses pour éviter le \ mal vu
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id ASC".format(state_name_searched)

    cursor.execute(query)

    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture des ressources
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_by_user_input()
