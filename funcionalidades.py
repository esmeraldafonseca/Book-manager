import json
import ficheiro
import pandas as pd
from rich import print
from rich.table import Table
from datetime import date

livros = []
ano_atual = date.today().year #Usa a biblioteca datatime para pegar o ano actual
GENERO_LITERARIO = ["Romance", "Conto", "Novela", "Fabula", "Didatico"] 


def limpar_tela():
    """
    Limpa a tela do terminal atraves do comando clean que é roddo diretamente no os
    """
    import os
    os.system('clear')



def cabecalho(titulo):
    """
    Argumento: string 
    Cria cabeçalhos estilizados e com o titulo centralizado 
    """
    titulo_cap = titulo.capitalize()
    print("*" * 56)
    print("*", end="")
    print(f"[bold blue] {titulo_cap:^53}[/]", end="")
    print("*")
    print("*" * 56)


def adicionar_livros(livros):
    """
    Argumento: lista/ dicionario/ tupla
    Solicita ao utilizador os dados de um ou mais livros e adiciona-os à lista,
    guardando as alterações no ficheiro JSON.
    Retorna um ficheiro json com os dados recolhidos
    """

    
    
    inicio = True
    while inicio:
        limpar_tela()
        cabecalho("Adicionar livro")
        titulo = input("Titulo do livro: ")
        autor = input("Autor: ")

        
        while True:
            ano_de_publicação = input("Ano de publicação: ")
            if ano_de_publicação.isdigit() and len(ano_de_publicação) == 4:
                ano_de_publicação_int = int(ano_de_publicação)
                if ano_de_publicação_int <= ano_atual:
                    break     
                else:
                    print("[bold red]ERROR.[/]Data invalidade!")         
                
            else:
                print("[bold red]ERROR.[/] Valor invalido. Tente novamente.")
                
        
        while True:

            estado = input("Já leste esse livro?[S/N] ").upper()
            if estado == "S":
                lido = True
                break
            elif estado == "N":
                lido = False
                break
            else:
                print("[bold red]ERROR.[/] Valor invalido. Tente S para sim e N para não")
            
        
        while True:
            print("Genero literario:")
            for i in GENERO_LITERARIO:
                print(f"    -{i}")
            genero = input("Digite a sua escolha: ").strip() .capitalize()
            if genero not in GENERO_LITERARIO:
                print("[bold red]ERROR.[/] Opção invalida, tente uma das opções disponiveis.")
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

        
        while True: 
            condição = input("Quer adicionar mais um livro?[S/N]").upper()
           
            if condição == "S":
                break
            elif condição == "N":
                inicio = False
                input("\nPressione ENTER para continuar...")
                limpar_tela()
                break
            else:
                print("[bold red]ERROR.[/] Valor invalido. Tente S para sim e N para não")
    
                 
def limpar_lista(livros):
    """
    Argmento: lista/ dicionario/ tupla
    Retorna uma lista vazia
    """

    limpar_tela()
    cabecalho("Limpar lista")
    print ("Essa acção é [bold]IRRVERSIVEL[/]!" )
    condicao = input("Tens a certeza que queres eliminar a tua lista de livros?[S/N]: " ).upper()
    if condicao.strip() == "S":
        livros.clear()
        with open("livros.json", "w", encoding="utf-8") as ficheiro:
            json.dump([], ficheiro, indent=4) #verficar se a lista já está vazia, caso sim informar ao usuario,

        input("\nPressione ENTER para continuar...")
        limpar_tela()
    elif condicao.strip() == "N":
        input("\nPressione ENTER para continuar...")
        limpar_tela()
        return
    else :
        print("[bold red]ERROR.[/] Digite uma das opções validas")

def editar_livro(livros):
    """
    Argumento: livros (list): Lista de dicionários contendo os dados dos livros.
    Mostra todos os livros cadastrados e permite ao utilizador
    selecionar qual deseja editar.
    """

    #Verifica se existem livros cadastrados
    if not livros:
        print("Não existem livros para editar.")
        return

    limpar_tela()
    cabecalho("Editar livro")

    #Mostra a lista numerada de livros
    print("Livros disponíveis:\n")
    for indice, livro in enumerate(livros, start=1):
        print(f"    {indice} - {livro['Titulo']} ({livro['Autor']})")

    #Solicita ao utilizador o número do livro a editar
    while True:
        escolha = input("\nDigite o número do livro que deseja editar: ")

        if not escolha.isdigit():
            print("[bold red]ERROR.[/] Digite apenas números.")
            continue

        escolha = int(escolha)

        if 1 <= escolha <= len(livros):
            break
        else:
            print("[bold red]ERROR.[/] Número inválido. Escolha um livro da lista.")

    #Obtém o livro selecionado
    livro = livros[escolha - 1]

    print("\nLivro selecionado:")
    print(f"Título: {livro['Titulo']}")
    print(f"Autor: {livro['Autor']}")
    print(f"Ano de publicação: {livro['Ano de publicacao']}")
    print(f"Género literário: {livro['Genero literario']}")
    print(f"Estado: {'Lido' if livro['Estado'] else 'Não lido'}")

    
    novo_titulo = input(
        "\nDigite o novo título (pressione Enter para manter o atual): "
    ).strip()

    if novo_titulo:
        livro["Titulo"] = novo_titulo

    
    ficheiro.criar_livro(livros)

    print("\nLivro atualizado com sucesso.")
    limpar_tela()


def pesquisar_livro(livros):
    """
    Argumento: lista/ dicionario/ tupla
    Pergunta ao usuaria o titulo do livro que pretende encontrar e caso
    esse titulo exitas, retorna uma lista com os restantes dados do livro em questão
    """

    limpar_tela()
    cabecalho("Pesquisar livro")
    titulo = input(f"Digite o titulo do livro que pretendes encontrar: ").upper()
    encontrado = False
    for livro in livros:
        if titulo in livro["Titulo"].upper():
            print(f"Livro encontrado:\n     {livro['Titulo']} de {livro['Autor']} lançado em {livro['Ano de publicacao']}")
            encontrado = True
            input("\nPressione ENTER para continuar...")
            limpar_tela()

    if not encontrado:
        print("Não existem livros. Adiciona primeiro.")
        input("\nPressione ENTER para continuar...")
        limpar_tela()
        return
    

       
def listar_livros(livros):
    """
    Argumento: lista/ dicionario/ tupla
    Mostra os itens de livros em forma de tabela
    Retorna uma tabela estilizada de todos os livros listados no ficheiro json
    """

    limpar_tela()
    cabecalho("Listar livros")

    if not livros:
        print("Não existem livros cadastrados.")
        return

    df = pd.DataFrame(livros)

    table = Table(title="Livros")

    for coluna in df.columns:
        table.add_column(coluna)

    for _, linha in df.iterrows():
        table.add_row(*[str(valor) for valor in linha])

    print(table)

    input("\nPressione ENTER para continuar...")
    limpar_tela()
        


    
