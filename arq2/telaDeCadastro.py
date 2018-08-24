'''   "r" = modo de leitura,
"a" escrever,
"w" apaga, e depois escreve'''
option = 0
while option != 4:
    print('''Selecione a opção:
--------------------------------
1 - para cadastrar
2 - para listar
3 - para limpar e escrever
4 - para sair
--------------------------------
''')
    option = int(input('Insira um Nº:'))
    if option == 1:
        print("-------------------------------------------")
        arq = open("arquivos/nomes.txt","a")#trabalha com aquivo txt.
        #escrevendo na variável arq
        nome = input("informe seu nome completo: ")
        arq.write(nome+"\n")
        #Salva as modificações e salva o arquivo
        arq.close()

    elif option == 2:
        print("--------------cadastrados----------------------")
        arquivo = open("arquivos/nomes.txt","r")
        conteudo = arquivo.readlines()

        for x in range(0,len(conteudo)):
            print(conteudo[x])

        arquivo.close()
    elif option == 3:
        print("-------------criar do zero - apaga tudo---------")
        arq = open("arquivos/nomes.txt","w")#trabalha com aquivo txt.
        #escrevendo na variável arq
        nome = input("informe seu nome completo")
        arq.write(nome+"\n")
        #Salva as modificações e salva o arquivo
        arq.close()

#Open retorna um endereço para o arquivo



#read = Le o arquivo inteiro / readlines() é como uma lista
#fileid meenu > função guardar inf, > 1 opção para chamar a forca > usar biblioteca para importar a palavra aleatória >
