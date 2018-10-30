# from tal import *
def criarBD(conexao):
    cursor = conexao.cursor()
    sql ='''
    CREATE TABLE IF NOT EXISTS  usuario (
        nome text,
        login text,
        senha text
    );
    '''
    cursor.execute(sql)
    conexao.commit()

def inserir(conexao, nome, login, senha):
    cursor = conexao.cursor()
    sql = '''
    INSERT INTO usuario VALUES(
    '{}',
    '{}',
    '{}');
    '''.format(nome, login, senha)

    cursor.execute(sql)
    conexao.commit()
def listar(conexao):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario"
    cursor.execute(sql)
    usuarios = cursor.fetchall()

    for usr in usuarios:
        print("{} -{} -{}".format(usr[0],usr[1],usr[2]))
def localizar(conexao, numID):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario WHERE rowid = {}".format(numID)
    cursor.execute(sql)
    usuarios = cursor.fetchall()

    for usr in usuarios:
        print("{} -{} -{}".format(usr[0],usr[1],usr[2]))

def alterar(conexao, nome, login, senha, numID):
    cursor = conexao.cursor()
    sql = "UPDATE usuario SET nome = '{}', login ='{}', senha ='{}' WHERE rowid = {}".format(nome, login, senha, numID)
    cursor.execute(sql)
    conexao.commit()

def excluir(conexao, numID):
    cursor = conexao.cursor()
    sql = "DELETE FROM usuario WHERE rowid = {}".format(numID)
    cursor.execute(sql)
    conexao.commit()








import sqlite3
conexao = sqlite3.connect("teste.sqlite")

option = 10

while option != 0:
    print('''
1 - criar BD
2 - Inserir
3 - listar
4 - localizar
5 - alterar
6 - excluir
0 - sair
    ''')
    option = int(input("Insira a opção: "))

    if option == 1:
        criarBD(conexao)
    if option == 2:
        nome = input("Insira seu nome: ")
        login = input("Insira seu login: ")
        senha = input("Insira sua senha: ")
        inserir(conexao, nome, login, senha)
    if option == 3:
        listar(conexao)
    if option == 4:
        numID = int(input("Insira o ID para localizar"))
        localizar(conexao, numID)
    if option == 5:
        numID = int(input("Insira o ID para alterar"))
        nome = input("Insira seu nome: ")
        login = input("Insira seu login: ")
        senha = input("Insira sua senha: ")
        alterar(conexao, nome, login, senha, numID)
    if option == 6:
        numID = int(input("Insira o ID para excluir"))
        excluir(conexao, numID)
