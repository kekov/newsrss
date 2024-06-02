import os
import subprocess

class SSHKeyManager:
    """
    Classe pour gérer les clés SSH.

    Attributes:
        key_path (str): Le chemin du fichier de clé SSH.
    """

    def __init__(self, key_path: str) -> None:
        """
        Initialise le gestionnaire de clé SSH avec le chemin de la clé.

        Args:
            key_path (str): Le chemin du fichier de clé SSH.
        """
        self.key_path = key_path

    def add_key(self) -> None:
        """
        Ajoute la clé SSH à l'agent SSH.

        Cette méthode démarre l'agent SSH et ajoute la clé SSH spécifiée à l'agent.
        """
        # Démarrer l'agent SSH
        subprocess.run(['eval', '$(ssh-agent -s)'], shell=True, check=True)
        # Ajouter la clé SSH à l'agent
        subprocess.run(['ssh-add', self.key_path], check=True)
