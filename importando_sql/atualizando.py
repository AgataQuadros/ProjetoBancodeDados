import os
import sqlite3

conn = sqlite3.connect("c:\python_agata\ProjetoBancodeDados\importando_sql\sql_import.db")

cursor = conn.cursor()

os.system('cls')
nome_cliente = input("digite o nome do cliente: ")
nova_idade = int(input("digite a nova idade: "))

# atualisa a idade com base no nome do funciomario
cursor.execute("UPDATE clientes SET idade = ? WHERE nome = ?",
                (nova_idade, nome_cliente))

# salva as alterações no bd
conn.commit()
print("Dados atualizados com sucesso!")
conn.close()