import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/products')
def products():
    # 1. Récupération des paramètres de l'URL
    source = request.args.get('source')
    id_filter = request.args.get('id', type=int)
    
    products_list = []
    error = None

    # 2. Validation de la source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 3. Extraction des données selon la source
    try:
        if source == 'json':
            with open('products.json', 'r') as f:
                products_list = json.load(f)
        
        elif source == 'csv':
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products_list = [row for row in reader]
        
        elif source == 'sql':
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row  # Indispensable pour avoir des dictionnaires
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            products_list = [dict(row) for row in cursor.fetchall()]
            conn.close()

    except Exception:
        # En cas d'erreur de fichier ou de base de données
        return render_template('product_display.html', error="Database error")

    # 4. Filtrage par ID (appliqué à toutes les sources)
    if id_filter is not None:
        products_list = [p for p in products_list if int(p['id']) == id_filter]
        if not products_list:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
