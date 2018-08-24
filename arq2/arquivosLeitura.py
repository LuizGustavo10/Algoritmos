#Open retorna um endereço para o arquivo
'''   "r" = modo de leitura,
      "a" escrever,
      "w" apaga, e depois escreve'''
#fileid
arquivo = open("arquivos/nomes.txt","r")
conteudo = arquivo.readlines()

for x in range(0,len(conteudo)):
    print(conteudo[x])

arquivo.close()
