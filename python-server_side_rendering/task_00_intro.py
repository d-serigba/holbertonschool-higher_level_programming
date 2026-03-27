import os

def generate_invitations(template, attendees):
    # 1. Vérification des types d'entrée
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries, got {type(attendees).__name__}.")
        return

    # 2. Gestion des entrées vides
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Traitement de chaque participant
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Liste des placeholders à remplacer
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Récupération de la valeur ou "N/A" si manquante/None
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Remplacement dans le template
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # 4. Génération des fichiers de sortie
        filename = f"output_{i}.txt"
        
        # On vérifie si le fichier existe déjà (optionnel selon les instructions, mais recommandé)
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists and will be overwritten.")
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
