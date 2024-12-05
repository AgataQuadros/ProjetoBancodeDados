import sqlite3


conn = sqlite3.connect("c:/python_agata/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

dados_varios_clientes = []

cursor.executemany(
    "INSERT INTO clientes (nome,idade) VALUES (?,?)", dados_varios_clientes)
conn.commit()

conn.close()