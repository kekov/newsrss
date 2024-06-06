from git_module.git_auto import GitAutomation
from rss_reader.multi_rss_reader import MultiRSSReader
from rss_reader.rss_exporter_html import RSSExporterHTML
from rss_reader.rss_feed_parser import RSSFeedParser
from rss_reader.rss_reader import RSSReader
from rss_reader.rss_url_fetcher import RSSUrlFetcher

# Initialisation du fetcher pour récupérer les URLs RSS à partir d'une source
fetcher = RSSUrlFetcher('https://pastebin.com/raw/3Wn5B0Qy')
rss_urls = fetcher.fetch()

# extrait les différente catégorie présent dans les flux RSS
categories = set([rss_url.category for rss_url in rss_urls])
print(f"Categories: {categories}")

# création d'un dictionnaire pour chaque catégorie. La clé est la catégorie et la valeur est une liste des URL RSS
rss_urls_by_category = {category: [rss_url for rss_url in rss_urls if rss_url.category == category] for category in categories}

# création d'un dictionnaire de parsers pour chaque catégorie. La clé est la catégorie et la valeur est une liste de parsers
parsers_by_category = {category: [RSSFeedParser(rss_url) for rss_url in rss_urls_by_category[category]] for category in categories}

# création d'un dictionnaire de lecteurs pour chaque catégorie. La clé est la catégorie et la valeur est une liste de lecteurs
readers_by_category = {category: [RSSReader(parser, RSSExporterHTML()) for parser in parsers_by_category[category]] for category in categories}

# création d'un dictionnaire de MultiRSSReader pour chaque catégorie. La clé est la catégorie et la valeur est un MultiRSSReader
multi_readers_by_category = {category: MultiRSSReader(readers) for category, readers in readers_by_category.items()}

exporter = RSSExporterHTML()

# Initialisation de l'automatisation Git pour committer et pousser le fichier index.html qui contient les news mise à jour
key_path = '/home/franck/.ssh/github_kekov'
repo_path = '.'
automation = GitAutomation(key_path, repo_path)
commit_message = 'Mise à jour des news'

# Pour chaque catégorie, récupérer les éléments RSS agrégés et les exporter
for category, multi_reader in multi_readers_by_category.items():
    all_items = multi_reader.get_all_items()
    output_file = f"news/{category}.html"
    multi_reader.export_all_items(output_file)
    print(f"RSS feed for category '{category}' exported to {output_file}")
    automation.add_commit_and_push(f"news/{category}.html", commit_message)


# Création des parsers pour chaque URL RSS récupérée
# parsers = [RSSFeedParser(rss_url) for rss_url in rss_urls]

# Initialisation de l'exporteur (HTML dans ce cas, mais pourrait être JSON, CSV, etc.)


# Création des lecteurs RSS avec les parsers et l'exporteur
# readers = [RSSReader(parser, exporter) for parser in parsers]


# Initialisation du MultiRSSReader pour agréger les éléments de tous les lecteurs
# multi_reader = MultiRSSReader(readers)

# Récupération de tous les éléments RSS agrégés
# all_items = multi_reader.get_all_items()
#
# # Chemin du fichier de sortie pour l'export des éléments RSS
# output_file = "news/index.html"  # Remplacer par .json ou .csv selon la stratégie choisie
# multi_reader.export_all_items(output_file)
# print(f"RSS feed exported to {output_file}")

# Initialisation de l'automatisation Git pour committer et pousser le fichier index.html qui contient les news mise à jour

