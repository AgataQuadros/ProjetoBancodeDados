import os

os.system("cls")

def exibir_menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Passagens Aéreas ===")
        print("1. Criar conta")
        print("2. Cadastrar Voo")
        print("3. Consultar passagem")
        print("5. Atualizar Informação")
        print("6. Excluir Registro")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pass
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            pass
        elif opcao == '5':
            pass
        elif opcao == '6':
            pass
        elif opcao == '7':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")