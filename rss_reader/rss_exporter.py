from abc import ABC, abstractmethod
from typing import List
from .rss_item import RSSItem

class RSSExporter(ABC):
    """
    Classe abstraite pour exporter des éléments RSS.

    Methods:
        export(items: List[RSSItem], file_path: str) -> None:
            Méthode abstraite pour exporter des éléments RSS dans un fichier.
    """

    @abstractmethod
    def export(self, items: List[RSSItem], file_path: str) -> None:
        """
        Exporte les éléments RSS dans un fichier spécifié.

        Args:
            items (List[RSSItem]): La liste des éléments RSS à exporter.
            file_path (str): Le chemin du fichier dans lequel exporter les éléments RSS.
        """
        pass