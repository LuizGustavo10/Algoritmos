import sqlite3 #para se comunicar com Banco de Dados

#iniciar a conexão com o Banco de Dados
conexao = sqlite3.connect("aula28.sqlite")

#criar um meio de operar/executar o sql
cursor =  conexao.cursor()
#tabela contato / telefone

#monta o sql a ser executado
#se não envolve alguma operação é TEXT caso contrário é INT
sql = """
CREATE TABLE IF NOT EXISTS usuario(
    nome text,
    login text,
    senha text
);
"""
#EXECUTA UM sql
cursor.execute(sql)
nome = input("Insira o seu nome")
login = input("Insira o seu usuario")
senha = input("Insira o seu senha")

############ inserindo um registro ##################
sql = """
    INSERT INTO usuario VALUES(
    "{}",
    "{}",
    "{}"
);
""".format(nome, login, senha)
#agora execute
cursor.execute(sql)

#salvar
conexao.commit()
#não use o commit em select, não precisa






#fechando a conexão
conexao.close()
