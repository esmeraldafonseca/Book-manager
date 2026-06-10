import json
import ficheiro
import pandas as pd
from rich import print
from rich.panel import Panel
from rich.table import Table
from datetime import date

livros = []
ano_atual = date.today().year #Usa a biblioteca datatime para pegar o ano actual
GENERO_LITERARIO = ["Romance", "Conto", "Novela", "Fabula", "Didatico"] 


   
def mostrar_lista(livros):
        print("Livros disponíveis:\n")
        for indice, livro in enumerate(livros, start=1):
            print(f"    {indice} - {livro['Titulo']} ({livro['Autor']})")

def limpar_tela():
    """
    Limpa a tela do terminal atraves do comando clean que é rodado diretamente no os
    """
    import os

    input("\nPressione ENTER para continuar...")
    os.system('clear')

#Conjunto de funções que retornam mensagens de erros estilizadas
def erro1():
    CAIXA1 = Panel("[white]Obrigado/a pela preferencia, tenha um bom dia e boa leitua.[/] :gem_stone:", style="blue", width=30)
    print(CAIXA1)

def erro2():
    CAIXA2 = Panel("[bold red]ERROR![/]. [white] Opção inexistente. Tente novamente [/]" , style="blue", width=30)
    print(CAIXA2)

def erro3():
    CAIXA3 = Panel("[bold red]ERROR![/] [white] Valor invalido, por favor digite uma das opções validas([bold]NUMEROS[/])" , style="blue", width=30)
    print(CAIXA3)

def erro4():
    CAIXA4 = Panel("[bold red]ERROR![/].[white]Campo vazio! Tente novamente.[/]" , style="blue", width=30)
    print(CAIXA4)

def campo_vazio(variavel):
    """
    Verifica de a variavel está vazia ou não e retorna uma mensagem de erro
    Ideal para usar dentro de loops para validar dados
    """
    if not variavel:
        erro4()

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


        while True:

            titulo = input("Titulo do livro: ").strip()
            if not titulo:
                erro4()
            else:
                break

        while True:
            autor = input("Autor: ").strip()
            if not autor:
                erro4()
            else:
                break

        
        while True:
            ano_de_publicação = input("Ano de publicação: ").strip()
            
            

            if ano_de_publicação.isdigit():
                ano_de_publicação_int = int(ano_de_publicação)
                if ano_de_publicação_int <= ano_atual and len(ano_de_publicação) == 4:
                    break     
                else:
                    erro2()         
                
            else:
                erro2()
                
        
        while True:

            estado = input("Já leste esse livro?[S/N] ").upper()
        
            if estado == "S":
                lido = True
                break
            elif estado == "N":
                lido = False
                break
            else:
                erro2()
            
        
        while True:
            print("Genero literario:")
            for indice, itens in enumerate (GENERO_LITERARIO, start=1):
                print(f"    {indice} - {itens}")
            genero = input("Digite a sua escolha: ").strip()
            msg = Panel("[white]Livro adicionado com sucesso.[/]:gem_stone:", style="blue", width=30)
            match genero:
                case "1":
                    genero="Romance"
                    print(msg)
                    break
                case "2":
                    genero = "Conto"
                    print(msg)
                    break
                case "3":
                    genero="Novela"
                    print(msg)
                    break
                case "4":
                    genero = "Fabula"
                    print(msg)
                    break
                case "5":
                    genero="Didatico"
                    print(msg)
                    break
                case _:
                    erro2()
                    

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
                limpar_tela()
                break
            else:
                erro3()

    
                 
def limpar_lista(livros):
    """
    Argmento: lista/ dicionario/ tupla
    Retorna uma lista vazia
    """
    OPCOES = ["Apagar todos os livros", "Apagar livro"]

    T=True
    while T:
        limpar_tela()
        cabecalho("Limpar lista")
        if not livros:
            print("Não ha livros para apagar. Tente adicionar primeiro.")
            limpar_tela()
            return
        else:

            for itens, elementos in enumerate(OPCOES, start=1):
                print(f'    {itens}- {elementos}')
            
            opcao = input("Digite a sua escolha: ").strip()

            match opcao:
                case "1":
                    limpar_tela()
                    cabecalho("Limpar lista")
                    print ("Essa acção é [bold]IRRVERSIVEL[/]!" )
                    while True:
                        condicao = input("Tens a certeza que queres eliminar a tua lista de livros?[S/N]: " ).upper()
                        
                        if condicao.strip() == "S":
                            livros.clear()
                            with open("livros.json", "w", encoding="utf-8") as ficheiro:
                                json.dump([], ficheiro, indent=4) #verficar se a lista já está vazia, caso sim informar ao usuario,
                            limpar_tela()
                            break
                        
                        elif condicao.strip() == "N":
                            break
                    
                        else :
                            erro2()
                case "2":
                    
                    flag =True
                    while flag:
                        limpar_tela()
                        cabecalho("Limpar lista")
                        mostrar_lista(livros)
                        escolha = input("\nDigite o número do livro que deseja eliminar: ")
                        if not escolha.isdigit():
                            erro3()
                            continue
                        elif not escolha:
                            erro2()
                        

                        escolha = int(escolha)
                        if escolha < 1 or escolha > len(livros):
                            erro2()
                            continue
                        livros.pop(escolha -1)

                        
                        with open("livros.json", "w", encoding="utf-8") as f:
                            json.dump(livros, f, indent=4)
                        print(f"\n[bold]Livro removido com sucesso[/]")

                        while True:    
                            continuar = input("\nQuer eliminar mais um livro?[S/N]").upper()
                            if continuar == "S":
                                flag = False
                                break
                            elif continuar == "N":
                                limpar_tela()
                                flag = False
                                T=False
                                break
                            else:
                                erro3()

                case _:
                    erro2()
                    continue
        


def editar_livro(livros):
    """
    Argumento: livros (list): Lista de dicionários contendo os dados dos livros.
    Mostra todos os livros cadastrados e permite ao utilizador
    selecionar qual deseja editar.
    """


    limpar_tela()
    cabecalho("Editar livro")

    #Verifica se existem livros cadastrados
    if not livros:
        print("Não existem livros para editar. Tente adicionar primeiro")
        limpar_tela()
        return


    mostrar_lista(livros)

    #Solicita ao utilizador o número do livro a editar
    while True:
        escolha = input("\nDigite o número do livro que deseja editar: ")

        if not escolha.isdigit():
            erro3()


            continue

        escolha = int(escolha)

        if 1 <= escolha <= len(livros):
            break
        else:
            erro3()
            
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

    limpar_tela()
    cabecalho("Pesquisar livro")

    if not livros:
        print("Não existem livros. Tente adicionar primeiro.")
        limpar_tela()
        return

    while True:
        titulo = input(
            "Digite o título do livro que pretendes encontrar: "
        ).upper().strip()

        encontrado = False

        for livro in livros:
            if titulo in livro["Titulo"].upper():
                print(
                    f"\nLivro encontrado:\n"
                    f"     {livro['Titulo']} de {livro['Autor']} "
                    f"lançado em {livro['Ano de publicacao']}"
                )
                encontrado = True

        if not encontrado:
            print("Livro não encontrado.")

        condicao = input(
            "\nQuer pesquisar mais algum livro [S/N]?: "
        ).upper().strip()

        if condicao == "S":
            continue
        elif condicao == "N":
            limpar_tela()
            break
        else:
            erro2()

    

       
def listar_livros(livros):
    """
    Argumento: lista/ dicionario/ tupla
    Mostra os itens de livros em forma de tabela
    Retorna uma tabela estilizada de todos os livros listados no ficheiro json
    """

    limpar_tela()
    cabecalho("Listar livros")

    if not livros:
        print("Não existem livros cadastrados. Tente adicionar primeiro.")
        limpar_tela()
        return

    df = pd.DataFrame(livros)

    table = Table(title="Livros")

    for coluna in df.columns:
        table.add_column(coluna)

    for _, linha in df.iterrows():
        table.add_row(*[str(valor) for valor in linha])

    print(table)

    limpar_tela()
        

