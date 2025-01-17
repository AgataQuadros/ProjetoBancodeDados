import os 
import sqlite3
from prettytable import PrettyTable


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

def Consulta():
    pergunta = input("qual tabela consultar? ")

    if pergunta == "clientes":
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        conn.close()
        
        
    elif pergunta == "site":
        cursor.execute("SELECT * FROM site")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.feal_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        conn.close()
        
        
    elif pergunta == "destinos":
        cursor.execute("SELECT * FROM destinos")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.feal_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        conn.close()
        
        
    elif pergunta == "passagem":
        cursor.execute("SELECT * FROM passagem")
        resultados = cursor.fetchall()

        os.system('cls')

        tabela = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]

        tabela.feal_names = colunas

        for row in resultados:
            tabela.add_row(row)

        print(tabela)
        conn.close()
    
    else:
        print("Opção inválida. Tente novamente.")