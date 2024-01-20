import pandas as pd
import feedparser as fp
from newspaper import Article

def process_rss(url, category):
    # Charger les données du flux RSS
    data = fp.parse(url)

    # Initialiser les listes pour stocker les données
    titles, dates, url_site_links, image_urls = [], [], [], []

    # Itérer sur les entrées du flux RSS
    for item in data.entries:
        titles.append(item.title)
        dates.append(item.published)
        url_site_links.append(item.link)

        #Lien de l'image
        if 'links' in item:
            image_urls.append(item.links[1]["href"])
        else:
            image_urls.append(None)

    # Créer un DataFrame avec les données du flux RSS
    rss_df = pd.DataFrame({
        'title': titles,
        'date': dates,
        'lien': url_site_links,
        'image_link': image_urls,
        'category': [category] * len(titles)
    })

    # Télécharger le contenu des articles
    contents = []
    for link in rss_df['lien']:
        article = Article(link)
        article.download()
        article.parse()
        contents.append(article.text)

    rss_df['content'] = contents

    return rss_df

def process_multiple_rss(rss_dict):
    # Initialiser un DataFrame vide pour stocker toutes les données
    global_df = pd.DataFrame()

    # Itérer sur les catégories et les URLs des flux RSS
    for category, url in rss_dict.items():
        # Appeler la fonction pour traiter un flux RSS individuel
        category_df = process_rss(url, category)

        # Concaténer le DataFrame résultant avec le DataFrame global
        global_df = pd.concat([global_df, category_df], ignore_index=True)

    return global_df

def load_rss_data(file_path):
    # Charger le JSON en tant que DataFrame avec Pandas
    df = pd.read_json(file_path, orient='index')

    # Transformer le DataFrame en un dictionnaire
    rss_dict = df.to_dict()[0]

    return rss_dict


def save_results(json_name, df_name):
    # Lecture du fichier JSON existant avec lines=True pour chaque ligne comme un enregistrement
    df_transpose = pd.read_json(json_name, lines=True)

    # On regarde a chaque fois combien on rajoute d'articles
    print(df_transpose.shape)

    # Sélection des colonnes existantes dans df_name et concaténation avec df_transpose
    df_transpose = pd.concat([df_transpose, df_name[df_transpose.columns]], ignore_index=True)

    # Élimination des doublons basés sur l'ensemble des colonnes
    df_transpose = df_transpose.drop_duplicates()

    # On regarde a chaque fois combien on rajoute d'articles
    print(df_transpose.shape)
    
    # Écriture du DataFrame résultant dans le fichier JSON
    df_transpose.to_json(json_name, orient='records', lines=True)