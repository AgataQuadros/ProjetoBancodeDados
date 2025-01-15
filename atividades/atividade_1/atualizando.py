import os 
import sqlite3


conn = sqlite3.connect("c:/ProjetoBancodeDados/atividades/atividade_1/importando_sql.db")
cursor = conn.cursor()

os.system('cls')

def Atualiza():
    pergunta = input("qual tabela Atualizar? ")

    if pergunta == "cliente":

        nome_cliente = input("digite o nome do cliente: ")
        novo_numero = int(input("digite a novo numero: "))

        cursor.execute("UPDATE clientes SET telefone = ? WHERE nome = ?",
                        (novo_numero, nome_cliente))

    elif pergunta == "site":
        nome_compania = input("digite o nome da compania: ")
        novo_cupom = input("digite a novo cupom: ")

        cursor.execute("UPDATE site SET cupons = ? WHERE companias = ?",
                        (novo_cupom, nome_compania))
        
    elif pergunta == "destinos":
        nome_destino = input("digite o nome do Destino: ")
        novo_turistico = input("digite a novo ponto turistico: ")

        cursor.execute("UPDATE destinos SET pontos_turisticos = ? WHERE locais = ?",
                        (novo_turistico, nome_destino))

    elif pergunta == "passagem":
        nome_cliente = input("digite o nome do cliente: ")
        nova_data = input("digite a nova data: ")

        cursor.execute("UPDATE passagem SET data = ? WHERE nome_cliente = ?",
                        (nova_data, nome_cliente))
        
    else:
        print("Opção inválida. Tente novamente.")

# salva as alterações no bd
conn.commit()
print("Dados atualizados com sucesso!")
conn.close()