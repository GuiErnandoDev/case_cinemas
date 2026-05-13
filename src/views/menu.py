from src.controllers.filme_controller import FilmeController


controller = FilmeController()


def exibir_menu():

    while True:

        print("""
======== CASE CINEMAS ========

1 - Cadastrar Filme
2 - Listar Filmes
3 - Excluir Filmes              
0 - Sair

==============================
        """)

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.cadastrar_filme()

        elif opcao == "2":
            controller.listar_filmes()
            
        elif opcao == "3":
          controller.excluir_filme()    

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida!")
