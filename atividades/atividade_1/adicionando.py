
def Adiciona():
    import sqlite3
    conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
    cursor = conn.cursor()

    print('')
    print("=== Adicinando informações ===")
    print("1. Site")
    print("2. Usuario")
    print("3. Destinos")
    print("4. Passagem")
    print("6. Voltar ao menu")
    pergunta = input("ah qual tabela você deseja adicionar? ")

    if pergunta == "1":
        companias = input("adicione o nome da compania: ")
        destinos = input("adicione o destino: ")
        precos = input("adicione o preço: ")
        cupons = input("adicione o cupom: ")
        hoteis = input("adicione o hotel: ")

        cursor.executemany(
        "INSERT INTO site (companias, destinos, precos, cupons, hoteis) VALUES (?, ?, ?, ?, ?)", [(companias, destinos, precos, cupons, hoteis)])

    elif pergunta == "2":
        nome = input("adicione o nome: ")
        cpf = input("adicione o cpf: ")
        email = input("adicione o email: ")
        telefone = input("adicione o telefone: ")
        modo_pagamento = input("adicione o modo de pagamento: ")

        cursor.executemany(
        "INSERT INTO clientes (nome, cpf, email, telefone, modo_pagamento) VALUES (?, ?, ?, ?, ?)", [(nome, cpf, email, telefone, modo_pagamento)])

    elif pergunta == "3":
        locais = input("adicione o destino: ")
        aeroporto = input("adicione o aeroporto de pouso: ")
        pontos_turisticos =input("adicione o ponto turistico principal: ")

        cursor.executemany(
        "INSERT INTO destinos (locais, aeroporto, pontos_turisticos) VALUES (?, ?, ?)", [(locais, aeroporto, pontos_turisticos)])


    elif pergunta == "4":
        nome_cliente = input("adicione o destino: ")
        assento = input("adicione o assento: ")
        voo = input("adicione o voo: ")
        destino = input("adicione o destino: ")
        data = input("adicione a data da viagem: ")
        horario = input("adicione o horario da viagem: ")
        saida = input("adicione a saida: ")
        compania_id =input("adicione a compania: ")

        cursor.executemany(
        "INSERT INTO passagem (nome_cliente, assento, voo, destino, data, horario, saida, compania_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [(nome_cliente, assento, voo, destino, data, horario, saida, compania_id)])
        
    else:
        print("voltando...")
    
    conn.commit()
    conn.close()