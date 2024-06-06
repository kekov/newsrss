from rss_reader.rss_url import RSSUrl
from typing import List
import requests

class RSSUrlFetcher:
    """
    Classe pour récupérer et traiter les URLs RSS depuis une source donnée.

    Attributes:
        url (str): L'URL de la source à partir de laquelle récupérer les URLs RSS.
    """

    def __init__(self, url: str) -> None:
        """
        Initialise le fetcher avec l'URL de la source.

        Args:
            url (str): L'URL de la source.
        """
        self.url = url

    def fetch(self) -> List[RSSUrl]:
        """
        Récupère et traite les URLs RSS depuis la source.

        Returns:
            List[RSSUrl]: Une liste d'objets RSSUrl contenant les informations des flux RSS.
        """
        response = requests.get(self.url)
        response.raise_for_status()
        lines = response.text.split('\n')
        rss_urls = []
        for line in lines:
            if line:  # ignore empty lines
                sort_index, name, url, category = line.split(';')
                category = category.rstrip()  # remove trailing newline characters
                rss_url = RSSUrl(name, url, int(sort_index) , category)
                rss_urls.append(rss_url)
        return rss_urls
