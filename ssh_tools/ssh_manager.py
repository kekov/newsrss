import os
import subprocess


class SSHKeyManager:
    def __init__(self, key_path: str) -> None:
        self.key_path = key_path

    def add_key(self) -> None:
        # Démarrer l'agent SSH
        subprocess.run(['eval', '$(ssh-agent -s)'], shell=True, check=True)
        # Ajouter la clé SSH à l'agent
        subprocess.run(['ssh-add', self.key_path], check=True)

# class SSHKeyManager:
#     def __init__(self, key_path: str) -> None:
#         self.key_path = key_path
#
#     def add_key(self) -> None:
#         # Démarrer l'agent SSH et capturer l'environnement
#         result = subprocess.run(['ssh-agent', '-s'], stdout=subprocess.PIPE, shell=True, check=True)
#         agent_output = result.stdout.decode('utf-8')
#
#         # Extraire les variables d'environnement de l'agent SSH
#         for line in agent_output.splitlines():
#             if line.startswith('SSH_AUTH_SOCK'):
#                 sock_path = line.split('=')[1].split(';')[0]
#                 os.environ['SSH_AUTH_SOCK'] = sock_path
#             elif line.startswith('SSH_AGENT_PID'):
#                 pid = line.split('=')[1].split(';')[0]
#                 os.environ['SSH_AGENT_PID'] = pid
#
#         # Ajouter la clé SSH à l'agent
#         subprocess.run(['ssh-add', self.key_path], check=True)
