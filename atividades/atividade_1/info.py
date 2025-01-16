import os 
import sqlite3
import consultando
import excluido
import adicionando
import atualizando


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

os.system('cls')

# nome, cpf, email, telefone, modo_pagamento, passagem