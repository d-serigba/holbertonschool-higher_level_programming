import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Fonctions de lecture des données ---

def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Transformation nécessaire pour le filtrage ultérieur
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def get_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        # LE SECRET : transforme les tuples en objets "dictionnaires"
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        # On convertit chaque ligne en vrai dictionnaire Python
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except sqlite3.Error:
        return None

# --- La Route Principale ---

@app.route('/products')
def products_display():
    source = request.args.get('source')
    # On force le type int pour l'ID dès la réception
    product_id = request.args.get('id', type=int)
    
    # 1. Validation de la source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Récupération selon la source
    products_list = []
    if source == 'json':
        products_list = get_json_data()
    elif source == 'csv':
        products_list = get_csv_data()
    elif source == 'sql':
        products_list = get_sql_data()
        if products_list is None:
            return render_template('product_display.html', error="Database error")

    # 3. Filtrage par ID
    if product_id is not None:
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
