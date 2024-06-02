from git import Repo

class GitCommand:
    def __init__(self, repo_path: str) -> None:
        self.repo = Repo(repo_path)

    def add(self, file_path: str) -> None:
        self.repo.index.add([file_path])

    def commit(self, message: str) -> None:
        self.repo.index.commit(message)

    def push(self, remote_name: str = 'origin', branch_name: str = 'main') -> None:
        remote = self.repo.remote(name=remote_name)
        remote.push(refspec=branch_name)



