from git_module.git_command import GitCommand
from ssh_tools.ssh_manager import SSHKeyManager


class GitAutomation:
    def __init__(self, key_path: str, repo_path: str) -> None:
        self.ssh_key_manager = SSHKeyManager(key_path)
        self.git_repo = GitCommand(repo_path)

    def commit_and_push(self, file_path: str, commit_message: str, remote: str = 'origin', branch: str = 'main') -> None:
        self.ssh_key_manager.add_key()
        self.git_repo.add(file_path)
        self.git_repo.commit(commit_message)
        self.git_repo.push(remote, branch)
