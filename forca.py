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
    print(" _" * len(escolhida)) #Esse é apenas o print Inicial, antes do laço de repetição
    print(listaDicas[x])

#inicio do código da forca...
reiniciar = 1
listaPalavras = [
"arvore","casa", "mercedes", "fitness", "fortnite", "mustang", "zebra","dinossauro","laranja","minecraft"]
listaDicas = [
"tem folhas...","serve de abrigo...", "marca de carro...", "academia...", "um jogo battle royale...", "um muscle car...", "um animal...","Um animal já extinto...","Uma cor...","Um jogo de construções..."]

while reiniciar == 1:
    # abaixo é -1 porque a lista começa em 0, se não tiver o -1 vai passar o tanto de posições, aqui estou trabalhando com posições
    x = posicao(0, len(listaPalavras)-1) #transferi o valor da função para a variavel "x"---------<----------<--------<--------<-------<----<-
    #pega o valor de "x" e verifica na lista a palavra, estão guarda uma palavra em escolhida
    escolhida = listaPalavras[x] # o "X" refere-se a posição escolhida, no caso escolhe uma palavra da lista

    #listas vazias para armazenar dados
    descobertas = []
    digitadas = []

    for c in range(0,len(escolhida)): #essa parte percorre cada letra da palavra escolhida aleatoriamente, uma palavra pode ser uma lista...
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
            print(listaDicas[x])

            for c in range(0, len(escolhida)):
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

    reiniciar = int(input("Insira (1) para jogar novamente e (2) para sair: "))
    if reiniciar == 2:
        break           #se o usuário escolher(2) sai do programa
# .upper
