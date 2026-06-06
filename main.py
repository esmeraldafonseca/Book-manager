"""
Projeto: Sistema de Gestão de Livros
Autora: Esmeralda Fonseca
Monitor: Sebilson Cristovão
Descrição: Aplicação em Python para gerir uma coleção de livros com armazenamento em JSON.
"""

import funcionalidades
import ficheiro
from rich import print
import art #Arte ASCII


inicio = True #flag variable
OPCOES = ["Adicionar livro", "Listar todos os livros", 
          "Pesquisar livro por titulo", "Editar ", "Apagar lista" , "Sair"]
livros = ficheiro.carregar_livros()




print(art.art)
print(f'Bem-vindo/a ao seu GESTOR DE LIVROS',)


#Menu principal
while inicio:
    funcionalidades.cabecalho("GESTOR DE LIVROS")
    print("Escolha uma das opções:")

    #loop que mostra as opções do menu
    for itens, elementos in enumerate(OPCOES, start=1):
        print(f'    {itens}- {elementos}')
        

    escolha = input("Digite a sua escolha: ").strip()


    try:
        escolha_int = int(escolha)
    except ValueError:
        funcionalidades.erro3()
        funcionalidades.limpar_tela()
        continue

    match escolha_int:
        case 1:
            funcionalidades.adicionar_livros(livros)
        case 2:
            funcionalidades.listar_livros(livros)
        case 3:
            funcionalidades.pesquisar_livro(livros)
        case 4:
            funcionalidades.editar_livro(livros)
        case 5:
            funcionalidades.limpar_lista(livros)
        case 6:
            print("")
            funcionalidades.erro1()
            funcionalidades.limpar_tela()
            inicio = False
        case _:
            print("")
            funcionalidades.erro2()

            funcionalidades.limpar_tela()


    
            

      

