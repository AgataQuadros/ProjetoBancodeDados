def Consulta():
    import os 
    import sqlite3
    from prettytable import PrettyTable


    conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
    cursor = conn.cursor()

    print('')
    print("=== Consultando informações ===")
    print("1. Site")
    print("2. Usuario")
    print("3. Destinos")
    print("4. Passagem")
    print("6. Voltar ao menu")
    pergunta = input("qual tabela consultar? ")

    if pergunta == "1":
        cursor.execute("SELECT * FROM site")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        conn.close()
        
        
    elif pergunta == "2":
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        
        
    elif pergunta == "3":
        cursor.execute("SELECT * FROM destinos")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        
        
    elif pergunta == "4":
        cursor.execute("SELECT * FROM passagem")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)

    
    else:
        print("voltando...")
        
    conn.close()