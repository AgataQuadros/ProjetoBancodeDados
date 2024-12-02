import os 
import sqlite3


conn = sqlite3.connect("c:/python_agata/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

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