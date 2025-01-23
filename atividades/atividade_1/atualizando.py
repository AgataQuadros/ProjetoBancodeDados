def Atualiza():
    import os 
    import sqlite3
    from prettytable import PrettyTable


    conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
    cursor = conn.cursor()

    os.system('cls')

    print('')
    print("=== Atualizando informações ===")
    print("1. Site")
    print("2. Usuario")
    print("3. Destinos")
    print("4. Passagem")
    print("6. Voltar ao menu")
    pergunta = input("qual tabela Atualizar? ")

    if pergunta == "1":
        nome_compania = input("digite o nome da compania: ")
        novo_cupom = input("digite a novo cupom: ")

        cursor.execute("UPDATE site SET cupons = ? WHERE companias = ?",
                        (novo_cupom, nome_compania))
        

    elif pergunta == "2":
        cursor.execute("SELECT nome FROM clientes")
        resultados = cursor.fetchall()

        tabela = PrettyTable()
        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        
        nome_cliente = input("digite o nome do cliente: ")
        novo_numero = int(input("digite a novo numero: "))

        cursor.execute("UPDATE clientes SET telefone = ? WHERE nome = ?",
                        (novo_numero, nome_cliente))

    elif pergunta == "3":
        nome_destino = input("digite o nome do Destino: ")
        novo_turistico = input("digite a novo ponto turistico: ")

        cursor.execute("UPDATE destinos SET pontos_turisticos = ? WHERE locais = ?",
                        (novo_turistico, nome_destino))

    elif pergunta == "4":
        nome_cliente = input("digite o nome do cliente: ")
        nova_data = input("digite a nova data: ")

        cursor.execute("UPDATE passagem SET data = ? WHERE nome_cliente = ?",
                        (nova_data, nome_cliente))
        
    else:
        print("voltando...")


    conn.commit()
    print("Dados atualizados com sucesso!")
    conn.close()