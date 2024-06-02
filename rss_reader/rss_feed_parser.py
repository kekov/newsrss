import requests
import xml.etree.ElementTree as ET
from typing import List
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .rss_item import RSSItem
from .rss_url import RSSUrl

class RSSFeedParser:
    """
    Classe pour parser les flux RSS et extraire les éléments.

    Attributes:
        rss_url (RSSUrl): L'objet RSSUrl contenant les informations du flux RSS.
    """

    def __init__(self, rss_url: RSSUrl) -> None:
        """
        Initialise le parser avec un objet RSSUrl.

        Args:
            rss_url (RSSUrl): L'objet RSSUrl contenant l'URL et les informations du flux RSS.
        """
        self.rss_url = rss_url

    def fetch_feed(self) -> str:
        """
        Récupère le flux RSS à partir de l'URL.

        Returns:
            str: Le contenu brut du flux RSS.
        """
        response = requests.get(self.rss_url.url)
        response.raise_for_status()
        return response.text

    def parse_feed(self, raw_feed: str) -> List[RSSItem]:
        """
        Parse le flux RSS brut pour en extraire les éléments.

        Args:
            raw_feed (str): Le contenu brut du flux RSS.

        Returns:
            List[RSSItem]: Une liste d'objets RSSItem extraits du flux.
        """
        root = ET.fromstring(raw_feed)
        items = []

        for item in root.findall('.//item'):
            date = item.find('pubDate').text if item.find('pubDate') is not None else None
            category = item.find('category').text if item.find('category') is not None else None
            title = item.find('title').text if item.find('title') is not None else None
            description_html = item.find('description').text if item.find('description') is not None else None
            url = item.find('link').text if item.find('link') is not None else None

            # Recherche de l'image dans les balises possibles
            image_url = None
            if item.find('media:content') is not None:
                image_url = item.find('media:content').get('url')
            elif item.find('enclosure') is not None:
                image_url = item.find('media:content').get('url')
            elif item.find('media:thumbnail') is not None:
                image_url = item.find('enclosure').get('url')

            # Si aucune image n'a été trouvée, rechercher une balise <img> dans le contenu encodé
            if image_url is None:
                content_encoded = item.find('{http://purl.org/rss/1.0/modules/content/}encoded').text if item.find(
                    '{http://purl.org/rss/1.0/modules/content/}encoded') is not None else None

                if content_encoded is not None:
                    soup = BeautifulSoup(content_encoded, 'html.parser')
                    img_tag = soup.find('img')
                    if img_tag is not None:
                        image_url = img_tag.get('src')

            # Si aucune image n'a été trouvée, rechercher une balise <img> dans la description
            if image_url is None and description_html is not None:
                soup = BeautifulSoup(description_html, 'html.parser')
                img_tag = soup.find('img')
                if img_tag is not None:
                    image_url = img_tag.get('src')

            description = self._clean_html(description_html) if description_html else None

            rss_item = RSSItem(self.rss_url, date, category, title, description, url, image_url)
            items.append(rss_item)

        return items

    def _is_image_url(self, url: str) -> bool:
        """
        Vérifie si l'URL pointe vers une image en vérifiant l'extension du fichier.

        Args:
            url (str): L'URL à vérifier.

        Returns:
            bool: True si l'URL pointe vers une image, sinon False.
        """
        parsed = urlparse(url)
        return any(parsed.path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif'])

    def _clean_html(self, raw_html: str) -> str:
        """
        Nettoie le contenu HTML pour ne garder que le texte.

        Args:
            raw_html (str): Le contenu HTML brut.

        Returns:
            str: Le contenu texte nettoyé.
        """
        soup = BeautifulSoup(raw_html, 'html.parser')
        return soup.get_text()
