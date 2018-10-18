# from tal inport *
import sqlite3

def criarBD(conexao):
    cursor = conexao.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS usuario(
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
    '{}'
    );
    '''.format(nome, login, senha)
    cursor.execute(sql)
    conexao.commit()

def listar(conexao):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario"
    cursor.execute(sql)

    usuarios = cursor.fetchall()
    for usr in usuarios:
        print("{} - {} - {}".format(usr[0],usr[1],usr[2]))

def localizar(conexao, nome):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario WHERE nome LIKE '{}' ".format(nome)
    cursor.execute(sql)

    usuarios =cursor.fetchall()
    for usr in usuarios:
        print("{} - {} - {}".format(usr[0],usr[1],usr[2]))
def alterar(conexao, numID, nome, login, senha):
    cursor = conexao.cursor()
    sql = "UPDATE usuario SET nome = '{}', login = '{}', senha = '{}' ".format(nome, login, senha)
    cursor.execute(sql)
    conexao.commit()

def excluir(conexao, numID):
    cursor = conexao.cursor()
    sql = "DELETE FROM usuario WHERE rowid = {} ".format(numID)
    cursor.execute(sql)
    conexao.commit()


conexao = sqlite3.connect("test.sqlite")


option= 10
while option != 0:
    print('''
1 - criar BD
2 - inserir
3 - listar
4 - localizar
5 - alterar
6 - excluir
0 - sair
    ''')
    option = int(input("Insira a opção"))
    if option == 1:
        criarBD(conexao)
    elif option == 2:
        nome = input("Insira seu nome: ")
        login = input("Insira seu login: ")
        senha = input("Insira sua senha: ")
        inserir(conexao, nome, login, senha)
    elif option == 3:
        listar(conexao)
    elif option == 4:
        nome = input("Insira o nome a ser localizado")
        localizar(conexao, nome)
    elif option == 5:
        numID = int(input("Insira o ID para alterar"))
        nome = input("Insira novo nome: ")
        login = input("Insira novo login: ")
        senha = input("Insira nova senha: ")
        alterar(conexao, numID, nome, login, senha)
    elif option == 6:
        numID = int(input("Insira o ID para alterar"))
        excluir(conexao, numID)


arq = open("arquivos/nome.txt","a")
nome = imput("Insira o nome")
arq.write(nome+"\n")
arq.close()



arq = open("arquivos/nome.txt","a")
conteudo = arquivo.readlines()

for x in range(0, len(conteudo))
    print(conteudo[x])
    listaPalavras.append(conteudo[x])
