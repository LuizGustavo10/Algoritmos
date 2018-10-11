#coesão/complemento = muito importante

from usuario import *
from outros import *
from contato import *

def fazer_login(conexao,login,senha):
    total = 0

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario WHERE login LIKE '{}'AND senha LIKE '{}';".format(login,senha) #use LIKE e não =
    cursor.execute(sql)

    contatos = cursor.fetchall()#vetor dentro de vetor, matrix
    tracejado_verde()
    for usr in contatos:
        print("\033[1;32m"+"id = {}\nnome = {}\nlogin = {}".format(usr[0],usr[1],usr[2])+"\033[m")
        print("\033[1;32m"+"Seja bem vindo {}!!".format(usr[1])+"\033[m")
        total+=1
    return total

login = input("Insira seu login")
senha = input("Insira sua Senha")
registros = fazer_login(conexao, login, senha)
if registros == 0:
    print("\033[1;33m"+"Não foram localizados registros!"+"\033[m")
else:

    option = 10
    while option != 0:


        print('''\033[1;36m
----------Menu Principal-----------+
1 - Contatos                       |
2 - Usuário                        |
0 - Sair                           |
-----------------------------------+\033[m''')
    #menu Principal
        option = int(input("Insira uma opção: "))
        if option == 1:
            menu_contatos()
        elif option == 2:
            menu_usuario()

    # Pelo que entendi, primeiro tem que ter uma parte de login que vai comparar
    # com os cadastros de login do banco de dados, mostrando em seguida o menu principal
