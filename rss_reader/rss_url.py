class RSSUrl:
    """
    Classe représentant une URL RSS avec ses attributs.

    Attributes:
        name (str): Le nom du flux RSS.
        url (str): L'URL du flux RSS.
        sort_index (int): L'indice de tri pour organiser les flux.
    """

    def __init__(self, name: str, url: str, sort_index: int) -> None:
        """
        Initialise un objet RSSUrl avec un nom, une URL et un indice de tri.

        Args:
            name (str): Le nom du flux RSS.
            url (str): L'URL du flux RSS.
            sort_index (int): L'indice de tri pour organiser les flux.
        """
        self.url = url
        self.name = name
        self.sort_index = sort_index

    def get_url(self) -> str:
        """
        Retourne l'URL du flux RSS.

        Returns:
            str: L'URL du flux RSS.
        """
        return self.url

    def get_name(self) -> str:
        """
        Retourne le nom du flux RSS.

        Returns:
            str: Le nom du flux RSS.
        """
        return self.name

    def get_sort_index(self) -> int:
        """
        Retourne l'indice de tri du flux RSS.

        Returns:
            int: L'indice de tri du flux RSS.
        """
        return self.sort_index
