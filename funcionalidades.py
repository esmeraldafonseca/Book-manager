import json
import ficheiro
import pandas as pd


livros=[]


def adicionar_livros(livros):

    """
    Criar um ficheiro para armazenar o titulo, autor, ano de publicação e genero
    return: um ficheiro com os dados recolhidos
    """


    inicio = True
    

    while inicio:
        print("1- ADICIONAR LIVRO")
        titulo = input("Titulo do livro: ")
        autor = input("Autor: ")

        while True:

            ano_de_publicação = input("Ano de publicação: ")
            if ano_de_publicação.isdigit() and len(ano_de_publicação) == 4:
                ano_de_publicação_int = int(ano_de_publicação)  
                break              
                
            else:
                print("ERROR. Valor invalido. Tente novamente.")
                

        while True:

            estado = input("Já leste esse livro?[S/N] ").upper()
            if estado == "S":
                lido = True
                break
            elif estado == "N":
                lido = False
                break
            else:
                print("ERROR. Valor invalido. Tente S para sim e N para não")
            

        genero = input("Genero literario: ")

        livro ={"Titulo": titulo,
                    "Autor": autor,
                    "Ano de publicacao": ano_de_publicação_int,
                    "Genero literario": genero,
                    "Estado": lido
                    }
        livros.append(livro)
        ficheiro.criar_livro(livros)

        while True: 
            condição = input("Quer adicionar mais um livro?[S/N]").upper()
           
            if condição == "S":
                break
            elif condição == "N":
                inicio = False
                break
            else:
                print("ERROR. Valor invalido. Tente S para sim e N para não")
    
                  
def limpar_lista(livros):
    
    condicao = input("Tens a certeza que queres eliminar a tua lista de livros?\n Essa acção é IRRVERSIVEL[S/N]").upper()
    
    if condicao.strip() == "S":
        livros.clear()
        with open("livros.json", "w", encoding="utf-8") as ficheiro:
            json.dump([], ficheiro, indent=4)
    

def editar_livro(livros):
    ...

def pesquisar_livro(livros):

    if not livros:
        print("Não existem livros. Adiciona primeiro.")
        return

    titulo = input(f"Digite o titulo do livro que pretendes encontrar: ").upper()
    for livro in livros:
        if titulo in livro["Titulo"]:
            print(f"{livro}: {livros}")
        else:
            print(f"ERROR.O livro com o titulo {titulo}, não foi encontrar. Tente novamente.")

def listar_livros(livros):
    print(f'Os seus livros sao:')
    tabela = pd.DataFrame(livros)
    return print("\n"* 5, tabela, "\n"*10)
    
