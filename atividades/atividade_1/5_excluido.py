import os 
import sqlite3


conn = sqlite3.connect("c:/python_agata/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

os.system('cls')

nome_cliente = input("Digite o nome do cliente para excluir: ")

cursor.execute("DELETE FROM clientes WHERE nome = ?", (nome_cliente,))
conn.commit()

print("cliente deletado com sucesso!")

conn.close()