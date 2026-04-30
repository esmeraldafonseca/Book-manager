import json
import ficheiro
import pandas as pd
from datetime import date

livros=[]
ano_atual = date.today().year
genero_literario = ["Romance", "Conto", "Novela", "Fabula", "Didatico"]

#
def limpar_tela():

    """
    """
    import os
    os.system('clear')


#
def cabecalho(titulo):
    """
    """
    print("*" * 56)
    print("*", end="")
    print(f"{titulo:^54}", end="")
    print("*")
    print("*" * 56)

#
def adicionar_livros(livros):
    """
    Criar um ficheiro para armazenar o titulo, autor, ano de publicação e genero
    return: um ficheiro com os dados recolhidos
    """

    
#
    inicio = True
    while inicio:
        limpar_tela()
        cabecalho("Adicionar livro")
        titulo = input("Titulo do livro: ")
        autor = input("Autor: ")

#
        while True:
            ano_de_publicação = input("Ano de publicação: ")
            if ano_de_publicação.isdigit() and len(ano_de_publicação) == 4:
                ano_de_publicação_int = int(ano_de_publicação)
                if ano_de_publicação_int <= ano_atual:
                    break     
                else:
                    print("ERRROR. Data invalidade!")         
                
            else:
                print("ERROR. Valor invalido. Tente novamente.")
                
#
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
            
#
        while True:
            print("Genero literario:")
            for i in genero_literario:
                print(f"    -{i}")
            genero = input("Digite a sua escolha: ").strip().upper()
            if genero not in genero_literario:
                print("ERROR. Opção invalida, tente uma das opções disponiveis.")
            else:
                genero = genero.title()
                break

        livro ={"Titulo": titulo,
                    "Autor": autor,
                    "Ano de publicacao": ano_de_publicação_int,
                    "Genero literario": genero,
                    "Estado": lido
                    }
        livros.append(livro)
        ficheiro.criar_livro(livros)

#
        while True: 
            condição = input("Quer adicionar mais um livro?[S/N]").upper()
           
            if condição == "S":
                break
            elif condição == "N":
                inicio = False
                break
            else:
                print("ERROR. Valor invalido. Tente S para sim e N para não")
    
 #                 
def limpar_lista(livros):
    """
    """

    limpar_tela()
    cabecalho("Limpar lista")
    condicao = input("Tens a certeza que queres eliminar a tua lista de livros?\n Essa acção é IRRVERSIVEL[S/N]").upper()
    
    if condicao.strip() == "S":
        livros.clear()
        with open("livros.json", "w", encoding="utf-8") as ficheiro:
            json.dump([], ficheiro, indent=4)
    
#
def editar_livro(livros):
    """
    """
    limpar_tela()
    cabecalho("Editar livro")


#
def pesquisar_livro(livros):
    """
    """

    limpar_tela()
    cabecalho("Pesquisar livro")
    titulo = input(f"Digite o titulo do livro que pretendes encontrar: ").upper()
    encontrado = False
    for livro in livros:
        if titulo in livro["Titulo"].upper():
            print(f"Livro encontrado: {livro["Titulo"]}")
            encontrado = True

        if not encontrado:
            print("Não existem livros. Adiciona primeiro.")
            return

#       
def listar_livros(livros):
    """
    """

    limpar_tela()
    cabecalho("Listar livros")
    print(f'Os seus livros sao:')
    tabela = pd.DataFrame(livros)
    return print("\n"* 5, tabela, "\n"*10)


    
