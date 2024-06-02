from typing import List
from rss_reader.rss_item import RSSItem
from rss_reader.rss_reader import RSSReader

class MultiRSSReader:
    """
    Classe pour gérer plusieurs lecteurs RSS et agréger leurs éléments.

    Attributes:
        readers (List[RSSReader]): Une liste de lecteurs RSS à partir desquels récupérer les éléments.
    """

    def __init__(self, readers: List[RSSReader]) -> None:
        """
        Initialise le MultiRSSReader avec une liste de lecteurs RSS.

        Args:
            readers (List[RSSReader]): La liste des lecteurs RSS.
        """
        self.readers = readers

    def get_all_items(self) -> List[RSSItem]:
        """
        Récupère tous les éléments des lecteurs RSS.

        Returns:
            List[RSSItem]: Une liste de tous les éléments RSS agrégés.
        """
        all_items = []
        for reader in self.readers:
            all_items.extend(reader.get_items())
        return all_items

    def export_all_items(self, file_path: str) -> None:
        """
        Exporte tous les éléments RSS triés dans un fichier spécifié.

        Args:
            file_path (str): Le chemin du fichier dans lequel exporter les éléments RSS.
        """
        all_items = sorted(self.get_all_items(), key=lambda x: (x.date.date(), x.rss_url.sort_index), reverse=True)
        self.readers[0].exporter.export(all_items, file_path)

