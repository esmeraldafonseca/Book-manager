import funcionalidades
import ficheiro
import art

inicio = True
opções = ["Adicionar livro", "Listar todos os livros", 
          "Pesquisar livro por titulo", "Editar ", "Apagar lista" , "Sair"]
livros = ficheiro.carregar_livros()


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
      

