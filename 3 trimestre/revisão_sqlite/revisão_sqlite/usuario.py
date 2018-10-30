from outros import *
def criar_tabela(conexao):
    cursor = conexao.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS usuario(
        nome text,
        login text,
        senha text
        );'''
    cursor.execute(sql)       #execuar
    conexao.commit()      #Gravar/salvar
def inserir(conexao, nome, login, senha):
    cursor = conexao.cursor()
    sql = '''INSERT INTO usuario VALUES(
        "{}",
        "{}",
        "{}"
        );
        '''.format(nome, login, senha)
    cursor.execute(sql)
    conexao.commit()

def listar(conexao):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario;"
    cursor.execute(sql)

    usuarios = cursor.fetchall() #vetor dentro de vetor

    for usr in usuarios:
        print("{} - {} - {}".format(usr[0],usr[1],usr[2]))

def localizar(conexao, nome):
    total = 0
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario WHERE nome LIKE '{}';".format(nome)
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for usr in usuarios:
        print("{} - {} - {}".format(usr[0],usr[1],usr[2]))
        total +=1
    if total == 0:
        print("Não foram encontrados registros")
def alterar(conexao, numId, nome, login, senha):
    cursor = conexao.cursor()
    sql = "UPDATE usuario SET nome = '{}', login = '{}', senha = '{}' WHERE rowid = {};".format(nome, login, senha, numId)
    cursor.execute(sql)
    conexao.commit()

def excluir(conexao, numId):
    cursor = conexao.cursor()
    sql = "DELETE FROM usuario WHERE rowid = {};".format(numId)
    cursor.execute(sql)
    conexao.commit()





import sqlite3
conexao = sqlite3.connect("BD.sqlite")

option = 10
while option != 0:
    print('''
1- criar tabela
2- inserir
3- listar
4- localizar
5- alterar
6- excluir
0- sair
    ''')

    option = int(input("Insira sua opção: "))

    if option == 1:
        criar_tabela(conexao)
    elif option == 2:
        nome = input("Insira seu nome: ")
        login = input("Insira seu login: ")
        senha = input("Insira sua senha: ")
        inserir(conexao, nome, login, senha)
    elif option == 3:
        listar(conexao)
    elif option == 4:
        nome = input("Insira o nome da pessoa a ser localizada: ")
        localizar(conexao,nome)
    elif option == 5:
        numId = int(input("Insira o id para localizar"))
        nome = input("Insira o novo nome: ")
        login = input("Insira o novo login: ")
        senha = input("Insira a nova senha: ")
        alterar(conexao, numId, nome, login, senha)
    elif option == 6:
        numId = int(input("Insira o id para localizar"))
        excluir(conexao,numId)
