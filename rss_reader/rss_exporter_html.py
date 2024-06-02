from typing import List
from .rss_item import RSSItem
from .rss_exporter import RSSExporter
from jinja2 import Environment, FileSystemLoader

class RSSExporterHTML(RSSExporter):
    """
    Classe pour exporter des éléments RSS dans un fichier HTML en utilisant Jinja2.

    Methods:
        export(items: List[RSSItem], file_path: str) -> None:
            Exporte les éléments RSS dans un fichier HTML.
    """

    def export(self, items: List[RSSItem], file_path: str) -> None:
        """
        Exporte les éléments RSS dans un fichier HTML spécifié.

        Args:
            items (List[RSSItem]): La liste des éléments RSS à exporter.
            file_path (str): Le chemin du fichier dans lequel exporter les éléments RSS.
        """
        # Créer un chargeur pour les templates Jinja2
        file_loader = FileSystemLoader('./template')  # Utilise le répertoire courant comme dossier de templates
        env = Environment(loader=file_loader)

        # Charger le template
        template = env.get_template('template.html')

        # Générer le HTML
        output = template.render(items=items)

        # Écrire le HTML dans le fichier
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(output)
