import sqlite3
import os

def create_database():
    db_name = 'products.db'
    
    # On se connecte (cela crée le fichier s'il n'existe pas)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # On crée la table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # On insère les données proprement
    # On utilise "INSERT OR REPLACE" pour éviter les erreurs si on relance le script
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Base de données créée avec succès !")

if __name__ == '__main__':
    create_database()
