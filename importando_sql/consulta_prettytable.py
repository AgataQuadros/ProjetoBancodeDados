import os
import sqlite3
from prettytable import PrettyTable # no terminal: pip install prettytable

conn = sqlite3.connect("c:\python_agata\ProjetoBancodeDados\importando_sql\sql_import.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')

# cria a table PrettyTable e define os nomes das colunas
tabela = PrettyTable()
# obtem os nomes das colunas PT
colunas = [descricao[0] for descricao in cursor.description]
# define on nomes das colunas na tabela PT
tabela.feal_names = colunas

# adiciona as linhas a tabela
for row in resultados:
    tabela.add_row(row)

print(tabela)
conn.close()