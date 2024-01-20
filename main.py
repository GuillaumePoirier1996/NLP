#from utils.scraping_utils import process_multiple_rss, load_rss_data, save_results
from pip import _internal

def main():
    try:
        _internal.main(['list'])
        # # Initialisation des variables
        # json_name = "francetvinfo_transformed.json"
        # json_name_2 = "tvinfo-sources.json"
        
        # # Charger les données depuis le fichier JSON
        # rss_dict = load_rss_data(json_name_2)

        # # Appeler la fonction pour traiter les flux RSS
        # result_df = process_multiple_rss(rss_dict)

        # # Enregistrer les résultats au format JSON
        # save_results(json_name, result_df)

        return True

    except Exception as e:
        # Affiche l'erreur (pour débogage) - vous pouvez la supprimer si vous ne souhaitez pas l'afficher
        print(f"Une erreur s'est produite : {str(e)}")

        # Retourne False en cas d'erreur
        return False

if __name__ == "__main__":
    main()
