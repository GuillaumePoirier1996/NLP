# Projet de Workflow GitHub Actions pour le Scraping
Ce projet vise à mettre en œuvre un workflow GitHub Actions permettant l'automatisation du scraping de données à partir de flux RSS. Le déclenchement du workflow est configuré toutes les 9 heures via une planification cron, mais également à chaque push sur le repo GitHub.

## Configuration du Workflow
Le fichier .github/workflows/scraping_workflow.yml définit le workflow, et voici quelques-unes de ses configurations principales :

```yaml 
name: Scraping Workflow

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 */9 * * *'
```

## Jobs du Workflow
Le workflow se compose d'un seul job, main.py, qui s'exécute sur une machine virtuelle Ubuntu. Avant l'exécution du script, la machine virtuelle est mise à jour et les dépendances spécifiées dans requirements.txt sont installées.

## Exécution du Code
Le script principal (main.py) contient la logique du scraping de données à partir de flux RSS. Il utilise des utilitaires définis dans le dossier utils.

## Utilitaires dans le Répertoire utils/scraping_utils.py
Le fichier scraping_utils.py dans le répertoire utils contient un ensemble de fonctions pour le scraping. Voici quelques-unes des fonctions importantes :

- process_rss(url, category): Fonction pour traiter un flux RSS individuel et renvoyer un DataFrame avec les données.
- process_multiple_rss(rss_dict): Fonction pour traiter plusieurs flux RSS et renvoyer un DataFrame global.

## Données d'Origine
Les données des flux RSS à scraper sont importées via fetch_transform_json.py. Deux fichiers JSON sont générés :

- tvinfo-sources.json: Contient un mapping des catégories aux URL des flux RSS.
- francetvinfo.json: Contient les données que l'on cherche à compléter en scrapant.

## Transformation
Les données sont transformées (transposées et réindexées) et complétées à chaque exécution du job. À chaque itération, les nouveaux articles sont récupérés, concaténés et les doublons sont éliminés.

## Remarques
Il est possible d'ajuster la planification cron dans le fichier de configuration du workflow selon les besoins. Pour une personnalisation supplémentaire, veuillez ajuster le fichier main.py et les utilitaires en conséquence.