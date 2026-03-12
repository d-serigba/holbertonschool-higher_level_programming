#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa.
Each row should display: (city_id, city_name, state_name)
"""
import MySQLdb
import sys


def list_cities():
    """
    Connects to the database and retrieves cities with their 
    corresponding state names using a JOIN.
    """
    # Connexion sécurisée
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # La jointure : on lie cities.state_id à states.id
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    INNER JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """
    
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
