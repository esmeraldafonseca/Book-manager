import json


def carregar_livros():
    """
    Carrega os livros armazenados no ficheiro JSON.
    Retorna uma lista vazia caso o ficheiro não exista.
    """

    try:
        with open("livros.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def criar_livro(livros):
    """
    Argmento: lista/ dicionario/ tupla
    Coleta os dados de livros e escreve dados no ficheiro json f
    """
    with open("livros.json", "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4)


def guardar_livro(livro):
    """
    Argmento: lista/ dicionario/ tupla
    Se guadar for sim, armazena os dados de livro no ficheiro json sem comprometer os ficheiros
    ja existentes, caso hajam
    """

    guardar = input(f"Deseja guardar os dados do livro {livro['Titulo']}? [S/N]").upper()
    if guardar == "S":
        try:
            with open("livros.json", "r", encoding="utf-8") as f:
                livros = json.load(f)
        except FileNotFoundError:
            livros = []
                
    else:
        return
