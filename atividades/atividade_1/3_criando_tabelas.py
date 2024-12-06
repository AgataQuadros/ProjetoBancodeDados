import sqlite3


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

# Tabela de clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf INTEGER NOT NULL,
        email TEXT NOT NULL,
        telefone INTEGER NOT NULL,
        modo_pagamento TEXT NOT NULL
    );
""")

# Tabela de site
cursor.execute("""
    CREATE TABLE IF NOT EXISTS site(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        companias TEXT NOT NULL,
        destinos TEXT NOT NULL,
        precos INTEGER NOT NULL,
        cupons TEXT NOT NULL,
        hoteis TEXT NOT NULL
    );
""")

# Tabela de passagem
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passagem(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        assento TEXT NOT NULL,
        voo INTEGER,
        destino TEXT NOT NULL,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        saida INTEGER NOT NULL,
        compania_id INTEGER NOT NULL,
        FOREIGN KEY (compania_id) REFERENCES site(id),
        FOREIGN KEY (nome_cliente) REFERENCES clientes(nome),
        FOREIGN KEY (destino) REFERENCES destinos(locais)
    );
""")

# Tabela de destinos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS destinos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        locais TEXT NOT NULL,
        aeroporto INTEGER NOT NULL,
        pontos_turisticos TEXT NOT NULL
    );
""")

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()