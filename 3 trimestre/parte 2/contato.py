# no Login, digitar login e senha, pegar login e senhar, buscar no
# Banco de dados se existe um usuario Like login que passou AND Like
# o que vc passou tbm,
# metodo login, buscar, format para monter conexaoexute, fetchall, usuarios =
#  cursor.fetchall, se o tamanho do vetor for 0, não existe. > que 0 tem algum cadastros
# usuario só alterar, contato, id nunca muda,
# pode ter um metodo chamado login, vai consultar no banco, vai passar o usuario e senha
 #u = login
#questão de niveis, nivel 0 estudante, 1 moderador, 2 professor...
#fetchall u = cursor.fetchall
# return u
# principal = login(chama o usuario\)

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

    sql = "SELECT rowid, * FROM contato;" #rowid é cada linha
    cursor.execute(sql)

    contatos = cursor.fetchall() #vetor dentro de vetor

    tracejado_verde()
    print("\033[1;32m"+"--------lista de usuarios-----------"+"\033[m")
    tracejado_verde()

    for usr in contatos: #matriz, lista dentro de lista
        print("\033[1;32m"+" {} - {} - {} - {} ".format(usr[0],usr[1],usr[2], usr[3])+"\033[m")
    tracejado_verde()

def localizar_cadastro(conexao,name):
    total = 0

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM contato WHERE nome LIKE '{}';".format(name) #use LIKE e não =
    cursor.execute(sql)

    contatos = cursor.fetchall()#vetor dentro de vetor, matrix
    tracejado_verde()
    for usr in contatos:
        print("\033[1;32m"+"{} - {} - {} - {}".format(usr[0],usr[1],usr[2],usr[3])+"\033[m")
        total+=1

    if total == 0:
        print("\033[1;33m"+"Não foram localizados registros!"+"\033[m")
    tracejado_verde()

def alterar_cadastro(conexao, new_name, new_fone, new_email, new_usuario):
    cursor = conexao.cursor()
    sql = "UPDATE usuario SET nome = '{}', fone = '{}', email = '{}', usuario = '{}' WHERE rowid = {};".format(new_name, new_login, new_senha, num_id)
    cursor.execute(sql)
    conexao.commit()

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
        elif option == 4:
            name = str(input("Insira o nome a ser localizado:"))
            localizar_cadastro(conexao,name)
        elif option == 5:
            executar = input("Tem certeza que deseja alterar? Dígite (S) para sim e (N) para não:").upper()
            if executar == "S":
                num_id = input("Insira o id da pessoa a ser alterada")
                new_name = str(input("Insira o novo nome para substituir: "))
                new_fone = str(input("Insira o novo telefone para substituir: "))
                new_email = str(input("Insira o novo Email para substituir: "))
                new_usuario = str(input("Insira o novo usuário para substituir: "))
                alterar_cadastro(conexao, new_name, new_fone, new_email, new_usuario)
            elif executar == "N":
                print("operação cancelada...")
