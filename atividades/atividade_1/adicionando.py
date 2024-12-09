import sqlite3


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

def Adiciona()
    pergunta = input("ah qual tabela você deseja adicionar? ")

    if pergunta == "cliente":
        nome = input("adicione o nome: ")
        cpf = input("adicione o cpf: ")
        email = input("adicione o email: ")
        telefone = input("adicione o telefone: ")
        modo_pagamento = input("adicione o modo de pagamento: ")
        dados_varios_clientes  = nome, cpf, email, telefone, modo_pagamento

        cursor.executemany(
        "INSERT INTO clientes (nome, cpf, email, telefone, modo_pagamento) VALUES (?, ?, ?, ?, ?)", dados_varios_clientes)
        conn.commit()

        conn.close()

    elif pergunta == "site":
        companias = input("adicione o nome da compania: ")
        destinos = input("adicione o destino: ")
        precos = input("adicione o preço: ")
        cupons = input("adicione o cupom: ")
        hoteis = input("adicione o hotel: ")
        dados_varias_informacoes = companias, destinos, precos, cupons, hoteis

        cursor.executemany(
        "INSERT INTO site (companias, destinos, precos, cupons, hoteis) VALUES (?, ?, ?, ?, ?)", dados_varias_informacoes)
        conn.commit()

        conn.close()

    elif pergunta == "destinos":
        locais = input("adicione o destino: ")
        aeroporto = input("adicione o aeroporto de pouso: ")
        pontos_turisticos =input("adicione o ponto turistico principal: ")
        dados_varios_destinos = [(locais, aeroporto, pontos_turisticos)]

        cursor.executemany(
        "INSERT INTO destinos (locais, aeroporto, pontos_turisticos) VALUES (?, ?, ?)", dados_varios_destinos)
        conn.commit()
        conn.close()

    elif pergunta == "passagem":
        nome_cliente = input("adicione o destino: ")
        assento = input("adicione o assento: ")
        voo = input("adicione o voo: ")
        destino = input("adicione o destino: ")
        data = input("adicione a data da viagem: ")
        horario = input("adicione o horario da viagem: ")
        saida = input("adicione a saida: ")
        compania_id =input("adicione a compania: ")
        dados_varias_passagens = nome_cliente, assento, voo, destino, data, horario, saida, compania_id

        cursor.executemany(
        "INSERT INTO passagem (nome_cliente, assento, voo, destino, data, horario, saida, compania_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", dados_varias_passagens)
        conn.commit()

        conn.close()
        
    else:
        print("Opção inválida. Tente novamente.")