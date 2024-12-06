import os 
import sqlite3
from prettytable import PrettyTable


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()


pergunta = input("qual tabela consultar? ")

if pergunta == "cliente":
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()

    os.system('cls')

    tabela = PrettyTable()

    colunas = [descricao[0] for descricao in cursor.description]

    tabela.feal_names = colunas

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