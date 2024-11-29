import os
import sqlite3

conn = sqlite3.connect("c:\python_agata\ProjetoBancodeDados\importando_sql\sql_import.db")

cursor = conn.cursor()

os.system('cls')

nome_cliente = input("Digite o nome do cliente para excluir: ")

# executa a exclusão com base no nome fornecido pelo usuario
cursor.execute("DELETE FROM clientes WHERE nome = ?", (nome_cliente,))
conn.commit()

print("cliente deletado com sucesso!")

# fecha a conexão
conn.close()
