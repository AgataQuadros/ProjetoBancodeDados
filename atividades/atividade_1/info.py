import os 
import sqlite3

conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

os.system('cls')

# nome, cpf, email, telefone, modo_pagamento, passagem
# pesquisar por nome e cpf, a pesquisara pricipalmente pelo cpf, assim se tiver alguem com o mesmo nome não me trará dor de cabeça
def Informação():
    nome_param = input('Entre com o nome do cliente: ')
    cpf_param = input('Entre com o cpf do cliente: ')

    # Executar o JOIN
    cursor.execute("""
        SELECT 
            clientes.nome,
            clientes.cpf,
            clientes.email,
            clientes.telefone,
            clientes.modo_pagamento,
            passagem.id AS passagem_id,
            passagem.assento,
            passagem.voo,
            passagem.destino,
            passagem.data,
            passagem.horario,
            passagem.saida
        FROM clientes
        LEFT JOIN passagem ON clientes.nome = passagem.nome_cliente
        WHERE clientes.cpf = ? OR (clientes.nome = ? AND ? IS NULL)
    """, (cpf_param, nome_param, cpf_param))

    # Obter os resultados
    resultados = cursor.fetchall()

    # Exibir os resultados
    for linha in resultados:
        print(linha)

    # Fechar a conexão
    conn.close()