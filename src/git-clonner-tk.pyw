import tkinter as tk
from tkinter import messagebox
import requests
import os
import subprocess

def clone_all_repos():
    username = username_entry.get()
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()

        if not os.path.exists(username):
            os.makedirs(username)
        os.chdir(username)

        for repo in repos:
            repo_name = repo['name']
            repo_url = repo['clone_url']
            subprocess.run(["git", "clone", "--recursive", repo_url])
        
        messagebox.showinfo("Concluído", "Todos os repositórios foram clonados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Clone Repositórios do GitHub")

# Criação dos widgets
username_label = tk.Label(root, text="Nome de usuário do GitHub:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)
clone_button = tk.Button(root, text="Clonar Repositórios", command=clone_all_repos)
clone_button.pack(pady=5)

# Execução da aplicação Tkinter
root.mainloop()
