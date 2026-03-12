#!/usr/bin/python3
"""
Lists all cities of a state provided as an argument.
Safe from SQL injections and uses only one execute().
"""
import MySQLdb
import sys


def filter_cities_by_state():
    """
    Connects to the database and retrieves cities associated
    with a specific state name.
    """
    # Connexion via les arguments passés au script
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Une seule requête avec JOIN pour respecter la contrainte 'execute() once'
    # Utilisation du paramètre %s pour la sécurité (D-Coy style)
    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()

    # Extraction des noms de villes (chaque ligne est un tuple d'un élément)
    # Puis jointure avec ", " pour le formatage final
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
