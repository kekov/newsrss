from datetime import datetime
from typing import Optional
from rss_reader.rss_url import RSSUrl

class RSSItem:
    """
    Classe représentant un élément RSS avec ses attributs.

    Attributes:
        rss_url (RSSUrl): L'URL RSS associé à l'élément.
        date (datetime): La date de publication de l'élément.
        category (str): La catégorie de l'élément.
        title (str): Le titre de l'élément.
        description (str): La description de l'élément.
        url (str): L'URL de l'élément.
        image_url (str): L'URL de l'image associée à l'élément.
    """

    def __init__(self, rss_url: RSSUrl, date: str, category: str, title: str, description: str, url: str, image_url: Optional[str]) -> None:
        """
        Initialise un élément RSS avec les informations fournies.

        Args:
            rss_url (RSSUrl): L'URL RSS associé à l'élément.
            date (str): La date de publication sous forme de chaîne.
            category (str): La catégorie de l'élément.
            title (str): Le titre de l'élément.
            description (str): La description de l'élément.
            url (str): L'URL de l'élément.
            image_url (Optional[str]): L'URL de l'image associée à l'élément.
        """
        self.rss_url = rss_url
        self.date = self._parse_date(date)
        self.category = category
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url if image_url else "https://raw.githubusercontent.com/kekov/newsrss/main/images/no_image.webp"

    def _parse_date(self, date_str: str) -> datetime:
        """
        Convertit une chaîne de date en objet datetime.

        Args:
            date_str (str): La chaîne de date à convertir.

        Returns:
            datetime: L'objet datetime correspondant.
        """
        date = datetime.today()
        for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
            try:
                date = datetime.strptime(date_str, fmt).replace(tzinfo=None)
                break
            except ValueError:
                continue
        return date

    def __repr__(self) -> str:
        """
        Représentation textuelle de l'élément RSS.

        Returns:
            str: Une chaîne décrivant l'élément RSS.
        """
        return f"RSSItem(name={self.rss_url.name}, date={self.date}, category={self.category}, title={self.title}, description={self.description}, url={self.url}, image_url={self.image_url})"
