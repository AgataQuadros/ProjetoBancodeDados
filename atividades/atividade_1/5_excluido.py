import os 
import sqlite3


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

os.system('cls')


pergunta = input("qual tabela consultar? ")

if pergunta == "cliente":
    nome_cliente = input("Digite o nome do cliente para excluir: ")

    cursor.execute("DELETE FROM clientes WHERE nome = ?", (nome_cliente,))
    conn.commit()

    print("cliente deletado com sucesso!")

    conn.close()
    
    
elif pergunta == "site":
    nome_cupom = input("Digite o cupom para não usar mais: ")

    cursor.execute("DELETE FROM site WHERE cupons = ?", (nome_cupom,))
    conn.commit()

    print("cupom deletado com sucesso!")

    conn.close()
    
    
elif pergunta == "destinos":
    ponto_turistico = input("Digite o ponto turistico para tirar do seu mapa: ")

    cursor.execute("DELETE FROM destinos WHERE pontos_turisticos = ?", (ponto_turistico,))
    conn.commit()

    print("ponto turistico deletado com sucesso!")

    conn.close()
    
    
elif pergunta == "passagem":
    assento = input("Digite o assento da passagem para cancelar: ")

    cursor.execute("DELETE FROM passagem WHERE assento = ?", (assento,))
    conn.commit()

    print("passagem cancelada com sucesso!")

    conn.close()