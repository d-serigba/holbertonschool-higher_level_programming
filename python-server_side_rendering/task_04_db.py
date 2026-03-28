import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Fonctions utilitaires de lecture ---

def get_sql_data(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            row = cursor.fetchone()
            return [dict(row)] if row else []
        else:
            cursor.execute('SELECT * FROM Products')
            return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# (Garder ici les fonctions read_json et read_csv de la tâche 3)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    products = []
    error = None

    # 1. Sélection de la source
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            error = "JSON file not found"
            
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                products = list(csv.DictReader(f))
        except FileNotFoundError:
            error = "CSV file not found"

    elif source == 'sql':
        products = get_sql_data(product_id)
        if products is None:
            error = "Database connection error"
        elif product_id and not products:
            error = "Product not found"
        # On saute le filtrage Python car le SQL s'en occupe déjà
        return render_template('product_display.html', products=products, error=error)

    else:
        error = "Wrong source"

    # 2. Filtrage pour JSON/CSV (si pas encore d'erreur)
    if not error and product_id is not None:
        products = [p for p in products if int(p['id']) == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
