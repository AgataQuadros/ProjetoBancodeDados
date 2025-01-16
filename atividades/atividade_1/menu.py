import os
import consultando
import excluido
import adicionando
import atualizando
import info


os.system("cls")


while True:
    print('')
    print("=== Sistema de Gerenciamento de Passagens Aéreas ===")
    print("1. Adicionar informações")
    print("2. Consultar tabelas")
    print("3. Atualizar Informação")
    print("4. Excluir Registro")
    print("5. Acessar todas as informações do cliente")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionando.Adiciona()
    elif opcao == '2':
        consultando.Consulta()
    elif opcao == '3':
        atualizando.Atualiza()
    elif opcao == '4':
        excluido.Exclui()
    elif opcao == '5':
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")