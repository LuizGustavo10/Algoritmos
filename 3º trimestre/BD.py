
# para vizualisar: http://inloop.github.io/sqlite-viewer/
import sqlite3
#funções
def criar_tabela_usuario(conexao): #cursor opera o BD

    cursor = conexao.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS usuario(
        nome text,
        login text,
        senha text
    );
    '''
    cursor.execute(sql)

def inserir_usuario(conexao):
    cursor = conexao.cursor()

    nome = input("Insira o seu nome")
    login = input("Insira o seu usuario")
    senha = input("Insira o seu senha")

    sql = """
        INSERT INTO usuario VALUES(
        "{}",
        "{}",
        "{}"
    );
    """.format(nome, login, senha)

    cursor.execute(sql)
    conexao.commit()

def listar_usuario(conexao):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM usuario;" #rowid a numeração de linha
    cursor.execute(sql)

    usuarios = cursor.fetchall() #buscar tudo, ele armazena todos os campos em uma linha do vetor

    for usr in usuarios:
        print("{}\t {} - {}".format(usr[0],usr[1],usr[2]))



#código principal
conexao = sqlite3.connect("aula28.sqlite")
# cursor = conexao.cursor()
listar_usuario(conexao)

#matriz

#for = para cada elemento da lista chama u
# select ...where nome like 'rafa', só onde o nome é rafa
# select ...where nome like '%rafa%', traz qualquer coisa que tenha rafa no começo ou no final...
