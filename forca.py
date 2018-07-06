from random import randint


listaPalavras = [
"arvore","casa", "mercedes", "fitness", "fortnite", "mustang", "zebra" ]

listaDicas = [
"tem folhas...","serve de abrigo...", "marca de carro...", "academia...", "um jogo battle royale...", "um muscle car...", "um animal..." ]


# Escolhe uma palavra da lista
x = randint(0,len(listaPalavras) - 1) # é -1 porque a lista começa em 0, se não tiver o -1 vai passar o tanto de posições, aqui estou trabalhando com posições

escolhida = listaPalavras[x]                    # o "X" refere-se a posição escolhida

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
            print("Você errou ! ")
            print("""
    ------
    |    O
    |
    |
    |
            """)

        elif erros == 2:
            print("""
    ------
    |    O
    |   /
    |
    |
            """)

        elif erros == 3:
            print("""
    ------
    |    O
    |   / \\
    |
    |
        """)
        elif erros == 4:
            print("""
    ------
    |    O
    |   /|\\
    |
    |
    |
    """)

        elif erros == 5:
            print("""
    ------
    |    O
    |   /|\\
    |   /
    |
    """)

        elif erros == 6:
            print("""
    ------
    |    O
    |   /|\\
    |   / \\
    |
            """)

        if erros == 7:
            print("Enforcado")
            break

        acertou = True
        for z in range(0, len(descobertas)):
            if descobertas[z] == "_":
                acertou = False #pula para trás se tiver algum tracinho

print(" ")
print("Parabéns!!!!")
# .upper
