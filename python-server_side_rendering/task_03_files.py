import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def read_csv(filepath):
    products = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # On convertit l'ID en int et le prix en float pour la cohérence
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    products = []
    error = None

    # 1. Vérification de la source
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        error = "Wrong source"

    # 2. Filtrage par ID si demandé et pas d'erreur de source
    if not error and product_id is not None:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            error = "Product not found"
        else:
            products = filtered_products

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
