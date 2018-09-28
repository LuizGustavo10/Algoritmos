from outros import *

def criar_tabela_contato(conexao):
    cursor = conexao.cursor()
    sql='''
    CREATE TABLE IF NOT EXISTS contato(
        nome text,
        fone text,
        email text,
        usuario integer /*será usado para chave estrangeira (ID)*/
    );
    '''
    cursor.execute(sql)
    conexao.commit()
def inserir_contato(conexao, nome, fone, email, usuario):
    cursor = conexao.cursor()
    sql = '''
    INSERT INTO contato VALUES(
    "{}",
    "{}",
    "{}",
    "{}"
    );
    '''.format(nome, fone, email, usuario)

    cursor.execute(sql)
    conexao.commit()

def listar_contato(conexao):
    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM contato;"
    cursor.execute(sql)

    contatos = cursor.fetchall() #vetor dentro de vetor

    tracejado_verde()
    print("\033[1;32m"+"--------lista de usuarios-----------"+"\033[m")
    tracejado_verde()

    for usr in contatos:
        print("\033[1;32m"+" {} - {} - {} - {} ".format(usr[0],usr[1],usr[2], usr[3])+"\033[m")
    tracejado_verde()


#============================================
def menu_contatos():
    conexao = sqlite3.connect("aula28.sqlite")
    option = 10
    while option != 0:
        print('''\033[1;36m
-----------Menu Contato------------+
1 - criar Banco de Dados           |
2 - Inserir novo cadastro          |
3 - Listar Contato                 |
4 - localizar um contato           |
5 - alterar um contato             |
6 - excluir um contato             |
0 - Voltar                         |
-----------------------------------+\033[m''')
        option = int(input("Insira uma opção: "))

        if option == 1:
            criar_tabela_contato(conexao)

        elif option == 2:
            nome = input("Insira seu Nome: ")
            fone = int(input("Insira seu telefone: "))
            email = input("Insira seu Email: ")
            usuario = input("Insira seu usuário: ")
            inserir_contato(conexao, nome, fone, email, usuario)
        elif option == 3:
            listar_contato(conexao)
