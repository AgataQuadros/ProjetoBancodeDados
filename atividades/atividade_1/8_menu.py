import os
import consultando
import excluindo
import adicionando
import atualizando


os.system("cls")


while True:
    print("\n=== Sistema de Gerenciamento de Passagens Aéreas ===")
    print("1. Adicionar informações")
    print("2. Consultar tabelas")
    print("3. Atualizar Informação")
    print("4. Excluir Registro")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    elif opcao == '1':
        adicionando.Adiciona()
    elif opcao == '2':
        consultando.Consulta()
    elif opcao == '3':
        atualizando.Atualiza()
    elif opcao == '4':
        excluindo.Exclui()
    elif opcao == '5':
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")