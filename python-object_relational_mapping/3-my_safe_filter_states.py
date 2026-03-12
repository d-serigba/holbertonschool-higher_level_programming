#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injections.
"""
import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to the DB and filters states using a parameterized query
    to prevent SQL injection.
    """
    # Récupération des arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion au serveur
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    # Utilisation de l'argument comme paramètre (le %s est géré par MySQLdb)
    # On ne met PAS de guillemets autour du %s, MySQLdb s'en occupe.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Nettoyage
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
