import sqlite3


conn = sqlite3.connect("c:/python_agata/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

dados_clientes = (cursor, "João Silva", 12345678901, "joao@gmail.com", 998765432, "Cartão de Crédito")
cursor.execute("INSERT INTO clientes (id, nome, cpf, email, telefone, modo_pagamento) VALUES (?, ?, ?, ?, ?, ?)", dados_clientes)

dados_site = (cursor, "Compania Aérea 1", "São Paulo", 1200, "CUPOM20", "Hotel A")
cursor.execute("INSERT INTO clientes (id, companias, destinos, precos, cupons, hoteis) VALUES (?, ?, ?, ?, ?, ?)", dados_site)

dados_passagem = (cursor, "João Silva", "12A", 101, "São Paulo", "2024-12-10", "10:30", 1, 1)
cursor.execute("INSERT INTO clientes (id, nome_cliente, assento, voo, destino, data, horario, saida, compania_id) VALUES (?, ?, ?, ?, ?, ?, ?,?, ?)", dados_passagem)

dados_destinos = (cursor, "São Paulo", 1, "Av. Paulista, Museu do Ipiranga")
cursor.execute("INSERT INTO clientes (id, locais, aeroporto, pontos_turisticos) VALUES (?, ?, ?, ?)", dados_destinos)


conn.commit()
conn.close()