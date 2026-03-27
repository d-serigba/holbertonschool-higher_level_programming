import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        # Lecture du fichier JSON
        with open('items.json', 'r') as f:
            data = json.load(f)
            # On récupère la liste associée à la clé "items"
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # En cas d'erreur de fichier, on envoie une liste vide
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
