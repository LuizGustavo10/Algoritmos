#Open retorna um endereço para o arquivo
'''   "r" = modo de leitura,
      "a" escrever,
      "w" apaga, e depois escreve'''
print("Abrindo arquivo...")
arq = open("arquivos/nomes.txt","a")#trabalha com aquivo txt.
print("Escrevendo no arquivo...")

#escrevendo na variável arq
nome = input("informe seu nome completo")
arq.write(nome+"\n")


print("Fechando o arquivo...")





#Salva as modificações e salva o arquivo
arq.close()
