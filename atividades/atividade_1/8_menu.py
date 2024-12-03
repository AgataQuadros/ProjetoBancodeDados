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
            cadastrar_passageiro()
        elif opcao == '2':
            cadastrar_voo()
        elif opcao == '3':
            emitir_passagem()
        elif opcao == '4':
            listar_passagens()
        elif opcao == '5':
            atualizar_informacao()
        elif opcao == '6':
            excluir_registro()
        elif opcao == '7':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")