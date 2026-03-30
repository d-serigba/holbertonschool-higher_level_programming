import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Validation immédiate de la source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    data = []
    try:
        if source == 'json':
            with open('products.json', 'r') as f:
                data = json.load(f)
        elif source == 'csv':
            with open('products.csv', 'r') as f:
                data = list(csv.DictReader(f))
        elif source == 'sql':
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            data = [dict(row) for row in cursor.fetchall()]
            conn.close()
    except Exception:
        return render_template('product_display.html', error="Database error")

    # 2. Filtrage par ID (on convertit en int pour être sûr)
    if product_id is not None:
        data = [p for p in data if int(p['id']) == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
