import sqlite3


conn = sqlite3.connect("c:/python_agata/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        nome TEXT NOT NULL PRIMARY KEY,
        cpf INTEGER NOT NULL,
        email TEXT NOT NULL,
        telefone INTEGER NOT NULL,
        modo_pagamento NOT NULL,
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS site(
        companias PRIMARY KEY AUTOINCREMENT,
        destinos TEXT NOT NULL,
        precos INTEGER NOT NULL,
        cupons TEXT NOT NULL,
        hoteis TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS passagem(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        assento TEXT NOT NULL,
        voo INTEGER,
        destinos TEXT NOT NULL,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        saida INTEGER NOT NULL,
        companias PRIMARY KEY AUTOINCREMENT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS destinos(
        locais TEXT NOT NULL PRIMARY KEY AUTOINCREMENT,
        aeroporto INTEGER NOT NULL,
        pontos_turisticos TEXT NOT NULL
    );
""")