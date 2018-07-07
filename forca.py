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
#inicio do código da forca...
reiniciar = 1
while reiniciar == 1:
    listaPalavras = [
    "arvore","casa", "mercedes", "fitness", "fortnite", "mustang", "zebra","dinossauro","laranja","minecraft"]
    listaDicas = [
    "tem folhas...","serve de abrigo...", "marca de carro...", "academia...", "um jogo battle royale...", "um muscle car...", "um animal...","Um animal já extinto...","Uma cor...","Um jogo de construções..."]

    # Escolhe uma palavra da lista
    x = randint(0,len(listaPalavras) - 1) # é -1 porque a lista começa em 0, se não tiver o -1 vai passar o tanto de posições, aqui estou trabalhando com posições
    escolhida = listaPalavras[x] # o "X" refere-se a posição escolhida

    #isso vai separar as letras da palavra, será usado em breve
    descobertas = []
    digitadas = []

    for c in range(0,len(escolhida)): #essa parte percorre cada letra da palavra escolhida aleatoriamente, uma palavra pode ser uma lista...
        descobertas.append("_") #append ??????????????????????????

    print(" _" * len(escolhida)) #Esse é apenas o print Inicial, antes do laço de repetição
    print(listaDicas[x])

    acertou = False
    erros = 0

    while acertou == False:
        acertos = 0
        print(" ")
        letra = input(str("Dígite uma letra: "))

        if letra in digitadas:
            print("Você já tentou essa letra !!") #verifica se a letra ja foi digitada, ainda falta arrumar
        else:
            digitadas.append(letra)
            print(listaDicas[x])

            for c in range(0, len(escolhida)):
                if letra == escolhida[c]:
                    descobertas[c] = letra
                    acertos+=1

                print(descobertas[c], end=' ')

            if acertos == 0:  #contador de erros, se não tiver nenhum acerto na rodada, mais um erro
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
                break

            acertou = True
            for z in range(0, len(descobertas)):
                if descobertas[z] == "_":
                    acertou = False #pula para trás se tiver algum tracinho

    if erros < 7:
        print(" ")
        ganhou()
        #se o erro for < 7 dá o parabéns
    reiniciar = int(input("Insira (1) para jogar novamente e (2) para sair: "))
    if reiniciar == 2:
        break           #se o usuário escolher(2) sai do programa
# .upper
