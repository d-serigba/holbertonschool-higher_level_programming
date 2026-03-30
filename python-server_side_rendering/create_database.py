import sqlite3
import os

def create_database():
    db_name = 'products.db'
    
    # LE BULLDOZER : Si le fichier existe, on le supprime de force
    # Cela règle l'erreur "file is not a database" à coup sûr.
    if os.path.exists(db_name):
        os.remove(db_name)
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Base de données reconstruite à neuf !")

if __name__ == '__main__':
    create_database()
