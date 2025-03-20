import subprocess
import pandas as pd
import json

# Fonction pour récupérer un fichier JSON avec wget
# "-0" permet de renommer le fichier json
# Ici, c'est pas vraiment utile mais je le laisse si je veux le changer plus tard
def fetch_json(url,json_name):
    try:
        subprocess.run(["wget", url, "-O", json_name])
        # Retourne True si tout s'est bien passé
        return True
    
    except Exception as e:
        # Affiche l'erreur (pour débogage) - vous pouvez la supprimer si vous ne souhaitez pas l'afficher
        print(f"Une erreur s'est produite : {str(e)}")

        # Retourne False en cas d'erreur
        return False

# Fonction de transformation du fichier
# Transposition et reindexation.
# Création de la colonne lien
def transform_json(json_name):
    try:
        # DataFrame à partir des données JSON avec réindexation
        df = pd.DataFrame(json.load(open(json_name))).transpose().reset_index().rename(columns={'index': 'lien'})
        
        # Suppression des colonnes 'author' et 'image_file'
        df = df.drop(['author', 'image_file'], axis=1)

        # Extraction du nom du fichier sans l'extension
        base_name = json_name.split('.')[0]

        # Ajout du suffixe '_transposed' et l'extension '.json'
        transposed_name = f"{base_name}_transformed.json"
        
        # Enregistrement du DataFrame au format json
        df.to_json(transposed_name, orient='records', lines=True)

        # Retourne True si tout s'est bien passé
        return True

    except Exception as e:
        # Affiche l'erreur (pour débogage) - vous pouvez la supprimer si vous ne souhaitez pas l'afficher
        print(f"Une erreur s'est produite : {str(e)}")

        # Retourne False en cas d'erreur
        return False

# Execution de la fonction
if __name__ == "__main__":
    # Liens des bases de données
    json_url = "https://people.irisa.fr/Guillaume.Gravier/teaching/ENSAI/data/francetvinfo.json"
    json_url_2 = "https://people.irisa.fr/Guillaume.Gravier/teaching/ENSAI/data/tvinfo-sources.json"

    # Noms
    json_name = "francetvinfo.json"
    json_name_2 = "tvinfo-sources.json"
    
    # Traitement du premier fichier
    fetch_json(json_url,json_name)
    transform_json(json_name)

    # Traitement du deuxième fichier
    fetch_json(json_url_2,json_name_2)