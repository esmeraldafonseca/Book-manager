<<<<<<< HEAD
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
=======
import funcionalidades
import ficheiro
import art

inicio = True
opções = ["Adicionar livro", "Listar todos os livros", 
>>>>>>> 293704a (feat:project upload)
          "Pesquisar livro por titulo", "Editar ", "Apagar lista" , "Sair"]
livros = ficheiro.carregar_livros()


<<<<<<< HEAD


print(f'Bem-vindo/a ao seu GESTOR DE LIVROS::',)
print(art.art)

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

    
            


    
=======
print("*" * 56)
print(f'{"GESTOR DE LIVROS":^56}')
print("*" * 56)
print(art.art)


while inicio:
    print(f'Bem-vindo/a ao GESTOR DE LIVROS, escolha uma das opções abaixo.',)
    for itens, elementos in enumerate(opções, start=1):
        print(f'{itens}- {elementos}')

    escolha = input("Digite a sua escolha: ").strip()

    if escolha == "":
        print("ERROR.Campo vazio!")
    else:

        try:
            escolha_int = int(escolha)
        except ValueError:
            print("ERROR! Valor invalido, por favor digite uma das opções validas(NUMEROS)")
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
            print("Obrigado/a pela preferencia, tenha um bom dia e boa leitua.")
            inicio = False
        else:
            print("")
            print("ERROR. Opção inexistente. Tente novamente ")
>>>>>>> 293704a (feat:project upload)
      

