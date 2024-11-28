import os
import sqlite3

conn = sqlite3.connect("c:\python_agata\ProjetoBancodeDados\importando_sql\sql_import.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)
conn.close()