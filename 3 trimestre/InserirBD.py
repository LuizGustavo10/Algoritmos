#fazer um menu para:
#reoganizar o código, para que fique certinho como em um menu
#listar, inserir, atualizar, exluir, localizar, where...
# para vizualisar: http://inloop.github.io/sqlite-viewer/

import sqlite3

def tracejado_verde():
    print("\033[1;32m"+"------------------------------------"+"\033[m")

def criar_tabela_usuario(conexao):

    sql ='''
    CREATE TABLE IF NOT EXISTS usuario(
        nome text,
        login text,
        senha text
    );
    '''
    cursor.execute(sql)
    conexao.commit()


def inserir_usuario(conexao, nome, login, senha):
    cursor = conexao.cursor()

    sql = '''
    INSERT INTO usuario VALUES(
    "{}",
    "{}",
    "{}"
    );
    '''.format(nome, login, senha)

    cursor.execute(sql)
    conexao.commit()

def listar_usuario(conexao):
    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario;"
    cursor.execute(sql)

    usuarios = cursor.fetchall() #vetor dentro de vetor

    tracejado_verde()
    print("\033[1;32m"+"--------lista de usuarios-----------"+"\033[m")
    tracejado_verde()

    for usr in usuarios:
        print("\033[1;32m"+" {} - {} - {} ".format(usr[0],usr[1],usr[2])+"\033[m")
    tracejado_verde()


def localizar_cadastro(conexao,name):
    total = 0

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario WHERE nome LIKE '{}';".format(name)
    cursor.execute(sql)

    usuario = cursor.fetchall()#vetor dentro de vetor, matrix
    tracejado_verde()
    for usr in usuario:
        print("\033[1;32m"+"{} - {} - {}".format(usr[0],usr[1],usr[2])+"\033[m")
        total+=1

    if total == 0:
        print("\033[1;33m"+"Não foram localizados registros!"+"\033[m")
    tracejado_verde()

def alterar_cadastro(conexao, num_id, new_name, new_login, new_senha):
    cursor = conexao.cursor()

    sql = "UPDATE usuario SET nome = '{}', login = '{}', senha = '{}' WHERE rowid = {};".format(new_name, new_login, new_senha, num_id)

    cursor.execute(sql)
    conexao.commit()

def excluir_cadastro(conexao, num_id):
    cursor = conexao.cursor()

    sql = "DELETE FROM usuario WHERE rowid = {}; ".format(num_id)
    cursor.execute(sql)
    conexao.commit()
#============================================================================

conexao = sqlite3.connect("aula28.sqlite")

option = 10
while option != 0:
    print('''\033[1;36m
-----------------Menu--------------+
1 - criar BD:                      |
2 - Inserir novo cadastro          |
3 - Listar cadastros               |
4 - localizar um cadastro          |
5 - alterar um cadastro            |
6 - excluir um cadastro            |
0 - sair                           |
-----------------------------------+\033[m''')
    option = int(input("Insira uma opção: "))

    if option == 1:
        criar_tabela_usuario(conexao)

    elif option == 2:
        nome = input("Insira seu Nome: ")
        login = input("Insira seu Login: ")
        senha = input("Insira sua Senha: ")
        inserir_usuario(conexao, nome, login, senha)

    elif option == 3:
        listar_usuario(conexao)

    elif option == 4:
        name = str(input("Insira o nome a ser localizado:"))
        localizar_cadastro(conexao,name)

    elif option == 5:
        num_id = input("Insira o id da pessoa a ser alterada")
        new_name = str(input("Insira o novo nome para substituir: "))
        new_login = str(input("Insira o novo login para substituir: "))
        new_senha = str(input("Insira a nova senha para substituir: "))
        alterar_cadastro(conexao, num_id, new_name, new_login, new_senha)

    elif option == 6:
        num = str(input("Insira o ID da pessoa a ser excluida: "))
        excluir_cadastro(conexao, num)

    else:
        print("opção Inválida!!!")

#MD5-------->HASH
#SHA!------->HASH
