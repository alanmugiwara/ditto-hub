import os
import subprocess

def clone_repositories(username):
    # Cria um diretório para armazenar os repositórios clonados
    os.makedirs(username, exist_ok=True)

    # Obtém a lista de repositórios do usuário
    response = subprocess.run(['curl', f'https://api.github.com/users/{username}/repos'], capture_output=True, text=True)
    repositories = response.stdout.split('"full_name": "')[1:]

    for repo in repositories:
        repo_name = repo.split('"')[0]
        # Clona o repositório
        subprocess.run(['git', 'clone', f'https://github.com/{repo_name}.git'], cwd=username)

if __name__ == "__main__":
    username = input("Digite o nome de usuário do GitHub: ")
    clone_repositories(username)
