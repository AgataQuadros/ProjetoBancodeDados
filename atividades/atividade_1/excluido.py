def Exclui():
    import os 
    import sqlite3


    conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
    cursor = conn.cursor()

    os.system('cls')

    print('')
    print("=== Excluindo informações ===")
    print("1. Site")
    print("2. Usuario")
    print("3. Destinos")
    print("4. Passagem")
    print("6. Voltar ao menu")
    pergunta = input("qual tabela consultar? ")

    if pergunta == "1":
        nome_cupom = input("Digite o cupom para não usar mais: ")

        cursor.execute("DELETE FROM site WHERE cupons = ?", (nome_cupom,))

        print("cupom deletado com sucesso!")

        
        
    elif pergunta == "2":
        nome_cliente = input("Digite o nome do cliente para excluir: ")

        cursor.execute("DELETE FROM clientes WHERE nome = ?", (nome_cliente,))

        print("cliente deletado com sucesso!")

        
        
    elif pergunta == "3":
        ponto_turistico = input("Digite o ponto turistico para tirar do seu mapa: ")

        cursor.execute("DELETE FROM destinos WHERE pontos_turisticos = ?", (ponto_turistico,))

        print("ponto turistico deletado com sucesso!")


        
        
    elif pergunta == "4":
        assento = input("Digite o assento da passagem para cancelar: ")

        cursor.execute("DELETE FROM passagem WHERE assento = ?", (assento,))
 

        print("passagem cancelada com sucesso!")


    
    else:
        print("voltando...")
    
    conn.commit()    
    conn.close()