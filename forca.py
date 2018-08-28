from random import randint
#relativo aos desenhos da forca, várias funções, o código está abaixo dos desenhos
def erro1():
    print("""

|─|─────────────────|
| |               (--)
| |
| |
| |
| |
| |
| |
|_|______________________
você tem 6 tentativas
─────────────────────────
""")
def erro2():
    print("""

|─|─────────────────|
| |               (oo)
| |                ||
| |                ||
| |                ||
| |
| |
| |
|_|______________________
você tem 5 tentativas
─────────────────────────
""")
def erro3():
    print("""

|─|─────────────────|
| |               (oo)
| |                ||_
| |                || \\
| |                ||  \\
| |
| |
| |
|_|______________________
você tem 4 tentativas
─────────────────────────
""")
def erro4():
    print("""

|─|─────────────────|
| |               (oo)
| |               _||_
| |              / || \\
| |             /  ||  \\
| |
| |
| |
|_|______________________
você tem 3 tentativas
─────────────────────────
""")
def erro5():
    print("""

|─|─────────────────|
| |               (oo)
| |               _||_
| |              / || \\
| |             /  ||  \\
| |                /
| |              _/
| |
|_|______________________
você tem 2 tentativas
─────────────────────────
""")
def erro6():
    print("""

|─|─────────────────|
| |               (oo)
| |               _||_
| |              / || \\
| |             /  ||  \\
| |                /\\
| |              _/  \\_
| |
|_|_______________________
você só tem 1 tentativa!!!
──────────────────────────
""")
def ganhou():
    print('''
----Parabéns!!!!------
───▐▀▄─────────▄▀▌───
───▐▓░▀▄▀▀▀▀▀▄▀░▓▌───
───▐░▓░▄▀░░░▀▄░▓░────
────█░░▌█▐░▌█▐░░█────
─▄▄▄▐▀░░░▀█▀░░░▀▌▄▄▄─
█▐▐▐▌▀▄░▀▄▀▄▀░▄▀▐▌▌▌█
▀▀▀▀▀▀▀▀▀▄▄▄▀▀▀▀▀▀▀▀▀
───Você ganhou !!!───
─────────────────────''')
def erro7():
    print('''
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼''')
#-----------FUNÇÃO RETORNO e PARÂMETRO-------
#abaixo está o seletor de posição, resposável por escolher uma determinada palavra da lista
def posicao(a,b):
    aleatorio = randint(a,b)
    return aleatorio #irá retornar para posicao o valor de "a", essa variavel só vale aqui dentro

def tracinhos_e_dicas():
    print("dica: ",listaDicas[x])
    print(" _" * (len(escolhida)-1)) #Esse é apenas o print Inicial, antes do laço de repetição

option = 0
while option != 4:
    print('''Selecione a opção:
--------------------------------
1 - para jogar
2 - para cadastrar
3 - para listar
4 - para sair
--------------------------------
''')
    option = int(input('Insira um Nº:'))
    if option == 1:
        #inicio do código da forca...

        listaPalavras = []
        listaDicas = []
        #inserindo palavras
        arq = open("arquivos/palavras.txt","r")
        conteudo = arq.readlines()
        for x in range(0,len(conteudo)):
            listaPalavras.append(conteudo[x])
        arq.close()
        #inserindo dicas
        arq = open("arquivos/dicas.txt","r")
        conteudo = arq.readlines()
        for x in range(0,len(conteudo)):
            listaDicas.append(conteudo[x])
        arq.close()



        reiniciar = "s"
        while reiniciar == "s":
            # abaixo é -1 porque a lista começa em 0, se não tiver o -1 vai passar o tanto de posições, aqui estou trabalhando com posições
            x = posicao(0, len(listaPalavras)-1) #transferi o valor da função para a variavel "x"---------<----------<--------<--------<-------<----<-
            #pega o valor de "x" e verifica na lista a palavra, estão guarda uma palavra em escolhida
            escolhida = listaPalavras[x] # o "X" refere-se a posição escolhida, no caso escolhe uma palavra da lista


            #listas vazias para armazenar dados
            descobertas = []
            digitadas = []

            #-1 por causa do bug da lista
            for c in range(0,len(escolhida)-1): #essa parte percorre cada letra da palavra escolhida aleatoriamente, uma palavra pode ser uma lista...
                descobertas.append("_") #coloca traço na lista vazia de descobertas

            tracinhos_e_dicas() #exibe os tracinhos iniciais e a dicas...

            acertou = False
            erros = 0

            while acertou == False:
                acertos = 0
                print(" ")
                letra = input(str("Dígite uma letra: ")).lower() #letra fica minúscula

                if letra in digitadas:
                    print("Você já tentou essa letra !!") #verifica se a letra ja foi digitada
                else:
                    digitadas.append(letra) # a letra vai para a lista de digitadas, para evitar repetições
                    print("--------------------------------")
                    print("Dica: ",listaDicas[x])

                    for c in range(0, len(escolhida)-1): #-1 por causa do bug da lista
                        if letra == escolhida[c]: #se alguma letra é igual a palavra da lista"escolhida"
                            descobertas[c] = letra #substitui o tracinho de descoberta pela letra
                            acertos+=1

                        print(descobertas[c], end=' ')

                    if acertos == 0:  #contador de erros, se não tiver nenhum acerto na rodada, soma mais um erro
                        erros+=1

                    if erros == 1:
                        erro1() #isso é uma função, relaciona com o desenho lá em cima
                    elif erros == 2:
                        erro2()
                    elif erros == 3:
                        erro3()
                    elif erros == 4:
                        erro4()
                    elif erros == 5:
                        erro5()
                    elif erros == 6:
                        erro6()
                    if erros == 7:
                        erro7()
                        break #sai do laço de repetição para dar fim no jogo

                    acertou = True # se chegou até aqui acertou fica TRUE
                    for z in range(0, len(descobertas)):
                        if descobertas[z] == "_":
                            acertou = False #pula lá para cima se tiver algum tracinho ainda

            if erros < 7: #se o erro for < 7 dá o parabéns
                print(" ")
                ganhou()

            reiniciar = str(input("Insira (s) para jogar novamente e (n) para sair: ")).lower()
            if reiniciar == "n":
                break           #se o usuário escolher(2) sai do programa
#Tela de cadastro
    if option == 2:
        print("------------Tela de Cadastro de palavras-----------------")
        print(" ")
        arq = open("arquivos/palavras.txt","a")#trabalha com aquivo txt.
        #escrevendo na variável arq
        palavraArq = input("informe a palavra a ser cadastrada: ")
        arq.writelines(palavraArq+"\n") #cuidade com write e writelines
        #Salva as modificações e salva o arquivo
        arq.close()
        print(" ")

        print("------------Tela de Cadastro de dicas-----------------")
        print(" ")
        arq = open("arquivos/dicas.txt","a")#trabalha com aquivo txt.
        #escrevendo na variável arq
        dicasArq = input("informe a dica a ser cadastrada: ")
        arq.writelines(dicasArq+"\n") #cuidade com write e writelines
        #Salva as modificações e salva o arquivo
        arq.close()
        print(" ")
    if option == 3:
        arq = open("arquivos/palavras.txt","r")
        conteudo = arq.readlines()
        for x in range(0,len(conteudo)):
            print(conteudo[x])
        arq.close()
    # if option == 4:
    # if option == 5:
# .upper
# listaPalavras = [
# "arvore","casa", "mercedes", "fitness", "fortnite", "mustang", "zebra","dinossauro","laranja","minecraft"]
# listaDicas = [
# "tem folhas...","serve de abrigo...", "marca de carro...", "academia...", "um jogo battle royale...", "um muscle car...", "um animal...","Um animal já extinto...","Uma cor...","Um jogo de construções..."]
