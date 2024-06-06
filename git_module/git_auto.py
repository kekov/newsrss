from git_module.git_command import GitCommand
from ssh_tools.ssh_manager import SSHKeyManager

class GitAutomation:
    """
    Classe pour automatiser les opérations Git avec gestion des clés SSH.

    Attributes:
        ssh_key_manager (SSHKeyManager): Le gestionnaire de clé SSH.
        git_repo (GitCommand): L'objet pour exécuter les commandes Git.
    """

    def __init__(self, key_path: str, repo_path: str) -> None:
        """
        Initialise l'automatisation Git avec le chemin de la clé SSH et le chemin du dépôt Git.

        Args:
            key_path (str): Le chemin du fichier de clé SSH.
            repo_path (str): Le chemin du dépôt Git.
        """
        self.ssh_key_manager = SSHKeyManager(key_path)
        self.git_repo = GitCommand(repo_path)

    def add_commit_and_push(self, file_path: str, commit_message: str, remote: str = 'origin', branch: str = 'main') -> None:
        """
        Ajoute, commit et push des changements Git en utilisant la clé SSH.

        Args:
            file_path (str): Le chemin du fichier à ajouter au commit.
            commit_message (str): Le message du commit.
            remote (str): Le nom du remote Git (par défaut 'origin').
            branch (str): Le nom de la branche Git (par défaut 'main').
        """
        self.ssh_key_manager.add_key()
        self.git_repo.add(file_path)
        self.git_repo.commit(commit_message)
        self.git_repo.push(remote, branch)
