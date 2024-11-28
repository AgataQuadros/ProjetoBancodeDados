import sqlite3

# conexão com BD
conn = sqlite3.connect("c:\python_agata\ProjetoBancodeDados\importando_sql\sql_import.db")

cursor = conn.cursor()

# definição de tupla com os dados
dados_cliente = ("João Silva", 30)

# placeholders (?,?): os pontoss de ? são usados como "espaço reservado", 
# eles serão substituidos pelos valores da tupla dados_cliente,
# por quê: usar placeholders é uma pratica recomendada
# pois previne ataques de injeção SQL.
cursor.execute("INSERT INTO clientes (nome,idade) VALUES (?,?)", dados_cliente)

conn.commit() # salva a transação no BD
conn.close() # fecha conexão