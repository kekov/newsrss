from git import Repo

class GitCommand:
    """
    Classe pour exécuter des commandes Git.

    Attributes:
        repo (Repo): L'objet représentant le dépôt Git.
    """

    def __init__(self, repo_path: str) -> None:
        """
        Initialise la commande Git avec le chemin du dépôt.

        Args:
            repo_path (str): Le chemin du dépôt Git.
        """
        self.repo = Repo(repo_path)

    def add(self, file_path: str) -> None:
        """
        Ajoute un fichier au commit.

        Args:
            file_path (str): Le chemin du fichier à ajouter.
        """
        self.repo.index.add([file_path])

    def commit(self, message: str) -> None:
        """
        Commit les changements avec un message.

        Args:
            message (str): Le message du commit.
        """
        self.repo.index.commit(message)

    def push(self, remote_name: str = 'origin', branch_name: str = 'main') -> None:
        """
        Push les changements vers le dépôt distant.

        Args:
            remote_name (str): Le nom du remote (par défaut 'origin').
            branch_name (str): Le nom de la branche (par défaut 'main').
        """
        remote = self.repo.remote(name=remote_name)
        remote.push(refspec=branch_name)
