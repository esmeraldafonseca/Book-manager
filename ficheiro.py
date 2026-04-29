import json

def carregar_livros():
    try:
        with open("livros.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def criar_livro(livros):
    with open("livros.json", "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4)

def guardar_livro(livro):

        guardar = input(f"Deseja guardar os dados do livro {livro['Titulo']}? [S/N]").upper()
        if guardar == "S":
            try:
                with open("livros.json", "r", encoding="utf-8") as f:
                    livros = json.load(f)
            except FileNotFoundError:
                livros = []
                
        else:
            return
