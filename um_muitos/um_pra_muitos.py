import sqlite3
from prettytable import PrettyTable
from pathlib import Path
import os


os.system('cls')


db_path = Path('um_muitos') / 'bd_rel_1_n.db'
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNUQUE NOT NULL,
    telefone TEXT,
    cidade TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    produto TEXT NOT NULL,
    quantidade TEXT UNUQUE NOT NULL,
    data TEXTNOT NULL,
    cidade TEXT NOT NULL,
    valor_total REAL NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
)
''')

# Função para verificar se o cliente existe no BD


def cliente_existe(id_cliente):
    cursor.execute(
        'SELECT 1 FROM Clientes WHERE id_cliente = ?', (id_cliente,))
    return cursor.fetchone() is not None

# Função para inserir dados a tabela Clientes


def inserir_cliente():
    nome = input( "Digite o nome do cliente: ")
    email = input( "Digite o email do cliente: ")
    telefone = input( "Digite o telefone do cliente: ")
    cidade = input( "Digite a cidade do cliente: ")
    cursor.execute('''
    INSERT INTO Clientes (nome, email, telefone, cidade)
    VALUES (?,?,?,?)
    ''', (nome, email, telefone, cidade))
    conn.commit()
    print('Cliente inserido com scesso!!!!')


# Função para inserir os dados na tabela Pedidos


def inserir_pedido():
    cursor.execute('''
    SELECT * FROM Clientes
    ''')
    resultados = cursor.fetchall()


    # Não pode fazer pedidos sem clientes
    if not resultados:
        print("- " * 70)
        print("Nenhum cliente encontrado. Cadastre um cliente primeiro.")
        print("- " * 70)

    tabela = PrettyTable(["id_cliente", "Nome", "Email", "Telefone", "Cidade"])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)
    
    try:
        #garantir q o id sema numeros inteiro
        id_cliente = int(input("Digite o ID do cliente: "))
        if not cliente_existe(id_cliente):
            print("- " * 70)
            print(f"Erro: cliente com ID {id_cliente} não encontrado!")
            print("Pr favor, cadastre o cliente primeiro.")
            print("- " * 70)
            return
        produto = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
        data = input("Digite a data do pedido (AAAA-MM-DD): ")
        valor_total = input("Digite o valor total do pedido: ")

        # Inserir o pedido no BD
        cursor.execute('''
        INSERT INTO pedido (id_cliente, produto, quantidade, data, valor_total) VALUES (?,?,?,?,?))''', (id_cliente, produto,quantidade, data, valor_total))
        conn.commit()

        print("Pedido inserido com sucesso !")
    except ValueError:
        print("- " * 70)
        print("Erro: ID do cliente deve ser um numero inteiro.")
        print("- " * 70)
    


# Função para realizar uma consulta com JOIN e exibir resultados
def consultar_pedidos():
    cursor.execute('''
    SELCT
        Clientes.nome, Clientes.email, Clientes.cidade, 
        Pedidos.produto, Pedidos.quantidade, Pedidos.valor_total
    FROM
        Clientes
    JOIN
        Pedidos on Clientes.id_cliente = Pedidos.id_cliente
    ''')
    resultados = cursor.fetchall()

    tabela = PrettyTable(
        ["Nome", "Email", "Telefone", "Cidade", "Produto", "Quantidade", "Valor Total"])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)


# Função para alterar um pedido existente
def alterar_pedido():
    try:
        id_pedido = int(input("Digite o ID do pedio que deseja altera: "))

        cursor.execute(
            'Select * FROM Pedidos Where id_pedido = ?', ((id_pedido,))
        )
        pedido = cursor.fetchall()

        if not pedido:
            print("- " * 70)
            print("Erro: ID do cliente {id_pedido} não encontrado!!!!")
            print("- " * 70)
        
         # Exibir os dados atuais do pedido:
        print('-'*70)
        print('Dados atuais do pedido:')
        print(f'Produto: {pedido[2]}')
        print(f'Quantidade: {pedido[3]}')
        print(f'Data: {pedido[4]}')
        print(f'Valor Total: {pedido[5]}')
        print('-'*70)
        
        # Solicitar novos dados do pedido:
        produto = input(
            'Digite o novo nome do produto (ou pressione Enter para manter o atual): ') or pedido[2]
        quantidade = input(
            'Digite a nova quantidade (ou pressione Enter para manter a atual): ') or pedido[3]
        data = input(
            'Digite a nova data (YYYY-MM-DD) (ou pressione Enter para manter a atual): ') or pedido[4]
        valor_total = input(
            'Digite o novo valor total (ou pressione Enter para manter o atual): ') or pedido[5]
        
        # Atualizar os dados do pedido:
        cursor.execute('''
        UPDATE Pedidos
        SET produto = ?, quantidade = ?, data = ?, valor_total = ?
        WHERE id_pedido = ?''',
        (produto, int(quantidade), data, float(valor_total), id_pedido))
        conn.commit()
        print('Pedido atualizado com sucesso!')

    except ValueError:
        print('-'*70)
        print('Erro: Entrada inválida.')
        print('-'*70)
        
# Menu interativo:
while True:
    print('\nMenu:')
    print('1. Inserir Cliente')
    print('2. Inserir Pedido')
    print('3. Consultar Pedidos')
    print('4. Alterar Pedido')
    print('5. Sair')
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        inserir_cliente()
    elif opcao == '2':
        inserir_pedido()
    elif opcao == '3':
        consultar_pedidos()
    elif opcao == '4':
        alterar_pedido()
    elif opcao == '5':
        print('Saindo...')
        break
    else:
        print('-'*70)
        print('Opção inválida. Tente novamente.')
        print('-'*70)

# Fechar a conexão com o banco de dados:
conn.close()