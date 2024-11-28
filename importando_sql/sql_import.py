import sqlite3

# conn: é a varialve para conexão com BD
conn = sqlite3.connect("c:\python_agata\ProjetoBancodeDados\importando_sql\sql_import.db")

# para operações no bd, você tambem precisara de um cursor,
# que é um objeto que permite executar comandos SQL
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
""")