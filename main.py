from git_module.git_auto import GitAutomation
from rss_reader.multi_rss_reader import MultiRSSReader
from rss_reader.rss_exporter_html import RSSExporterHTML
from rss_reader.rss_feed_parser import RSSFeedParser
from rss_reader.rss_reader import RSSReader
from rss_reader.rss_url_fetcher import RSSUrlFetcher

# Initialisation du fetcher pour récupérer les URLs RSS à partir d'une source
fetcher = RSSUrlFetcher('https://pastebin.com/raw/3Wn5B0Qy')
rss_urls = fetcher.fetch()

# Création des parsers pour chaque URL RSS récupérée
parsers = [RSSFeedParser(rss_url) for rss_url in rss_urls]

# Initialisation de l'exporteur (HTML dans ce cas, mais pourrait être JSON, CSV, etc.)
exporter = RSSExporterHTML()

# Création des lecteurs RSS avec les parsers et l'exporteur
readers = [RSSReader(parser, exporter) for parser in parsers]

# Initialisation du MultiRSSReader pour agréger les éléments de tous les lecteurs
multi_reader = MultiRSSReader(readers)

# Récupération de tous les éléments RSS agrégés
all_items = multi_reader.get_all_items()

# Chemin du fichier de sortie pour l'export des éléments RSS
output_file = "news/index.html"  # Remplacer par .json ou .csv selon la stratégie choisie
multi_reader.export_all_items(output_file)
print(f"RSS feed exported to {output_file}")

# Initialisation de l'automatisation Git pour committer et pousser le fichier index.html qui contient les news mise à jour
key_path = '/home/franck/.ssh/github_kekov'
repo_path = '.'
file_path = 'news/index.html'
commit_message = 'Mise à jour des news'

automation = GitAutomation(key_path, repo_path)
automation.commit_and_push(file_path, commit_message)
