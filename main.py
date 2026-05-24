"""
Projeto: Sistema de Gestão de Livros
Autora: Esmeralda Fonseca
Monitor: Sebilson Cristovão
Descrição: Aplicação em Python para gerir uma coleção de livros com armazenamento em JSON.
"""

import funcionalidades
import ficheiro
from rich import print
from rich.panel import Panel
import art #Arte ASCII


inicio = True #flag variable
CAIXA1 = Panel("[white]Obrigado/a pela preferencia, tenha um bom dia e boa leitua.[/] :gem_stone:", style="blue", width=30)
CAIXA2 = Panel("[bold red]ERROR![/]. [white] Opção inexistente. Tente novamente [/]" , style="blue", width=30)
CAIXA3 = Panel("[bold red]ERROR![/] [white] Valor invalido, por favor digite uma das opções validas([bold]NUMEROS[/])" , style="blue", width=30)
CAIXA4 = Panel("[bold red]ERROR![/].[white]Campo vazio![/]" , style="blue", width=30)
OPCOES = ["Adicionar livro", "Listar todos os livros", 
          "Pesquisar livro por titulo", "Editar ", "Apagar lista" , "Sair"]
livros = ficheiro.carregar_livros()


funcionalidades.cabecalho("GESTOR DE LIVROS")
print(art.art)

print(f'Bem-vindo/a ao seu GESTOR DE LIVROS, escolha uma das opções abaixo.',)

#Menu principal
while inicio:
    print("Escolha uma das opções:")

    #loop que mostra as opções do menu
    for itens, elementos in enumerate(OPCOES, start=1):
        print(f'    {itens}- {elementos}')
        

    escolha = input("Digite a sua escolha: ").strip()

    if escolha == "":
        print(CAIXA4)
    else:

        try:
            escolha_int = int(escolha)
        except ValueError:
            print(CAIXA3)
            funcionalidades.limpar_tela()
            continue
        if escolha_int == 1:
            funcionalidades.adicionar_livros(livros)
        elif escolha_int == 2:
            funcionalidades.listar_livros(livros)
        elif escolha_int == 3:
            funcionalidades.pesquisar_livro(livros)
        elif escolha_int == 4:
            funcionalidades.editar_livro(livros)
        elif escolha_int == 5:
            funcionalidades.limpar_lista(livros)
        elif escolha_int == 6:
            print("")
            
            print(CAIXA1)
            inicio = False
        else:
            print("")
            print(CAIXA2)
            funcionalidades.limpar_tela()


    
      

