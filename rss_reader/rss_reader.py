from typing import List
from .rss_exporter import RSSExporter
from .rss_feed_parser import RSSFeedParser
from .rss_item import RSSItem

class RSSReader:
    """
    Classe pour lire et gérer les flux RSS.

    Attributes:
        parser (RSSFeedParser): Le parser pour récupérer et analyser le flux RSS.
        exporter (RSSExporter): L'exportateur pour exporter les éléments RSS.
    """

    def __init__(self, parser: RSSFeedParser, exporter: RSSExporter) -> None:
        """
        Initialise le lecteur RSS avec un parser et un exportateur.

        Args:
            parser (RSSFeedParser): Le parser pour récupérer et analyser le flux RSS.
            exporter (RSSExporter): L'exportateur pour exporter les éléments RSS.
        """
        self.parser = parser
        self.exporter = exporter

    def get_items(self) -> List[RSSItem]:
        """
        Récupère les éléments RSS du flux.

        Returns:
            List[RSSItem]: Une liste d'objets RSSItem.
        """
        raw_feed = self.parser.fetch_feed()
        return self.parser.parse_feed(raw_feed)

    def display_items(self, items: List[RSSItem]) -> None:
        """
        Affiche les éléments RSS.

        Args:
            items (List[RSSItem]): La liste des éléments RSS à afficher.
        """
        for item in items:
            print(item)

    def export_items(self, items: List[RSSItem], file_path: str) -> None:
        """
        Exporte les éléments RSS dans un fichier.

        Args:
            items (List[RSSItem]): La liste des éléments RSS à exporter.
            file_path (str): Le chemin du fichier dans lequel exporter les éléments RSS.
        """
        self.exporter.export(items, file_path)
