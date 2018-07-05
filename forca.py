from random import randint
listaPalavras = [
"arvore","casa", "mercedes", "fitness", "fortnite", "mustang", "zebra" ]

listaDicas = [
"tem folhas...","serve de abrigo...", "marca de carro...", "academia...", "um jogo battle royale...", "um muscle car...", "um animal..." ]

# Escolhe uma palavra da lista
x = randint(0,len(listaPalavras) - 1) # é -1 porque a lista começa em 0, se não tiver o -1 vai passar o tanto de posições, aqui estou trabalhando com posições
# z = randint(0,len(listaDicas) - 1)
escolhida = listaPalavras[x]                    # o "X" refere-se a posição escolhida
#escolhida_dicas = listaDicas[z]

#isso vai separar as letras da palavra, será usado em breve

descobertas = []

for c in range(0,len(escolhida)): #essa parte percorre cada letra da palavra escolhida aleatoriamente, uma palavra pode ser uma lista...
    descobertas.append("_") #append ??????????????????????????

print(" _" * len(escolhida)) #Esse é apenas o print Inicial, antes do laço de repetição

acertou = False
erros = 0

while acertou == False:
    acertos = 0
    print(" ")
    letra = input(str("Dígite uma letra: "))
    print(listaDicas[x])

    for c in range(0, len(escolhida)):


        if letra == escolhida[c]:
            descobertas[c] = letra
            acertos+=1

        print(descobertas[c], end=' ')

    if acertos == 0:  #contador de erros, se não tiver nenhum acerto na rodada, mais um erro
        erros+=1

    acertou = True
    for z in range(0, len(descobertas)):
        if descobertas[z] == "_":
            acertou = False #pula para trás se tiver algum tracinho

print(" ")
print(erros)
print("Parabéns!!!!")


# # apenas outro modo de separar a palavra
# p = 0
# while p < len(escolhida):
#     print(escolhida[p])
#     p += 1
#
#
#
# for c in range (0, len(listaPalavras)): #o "c" seria como o p, onde p = p+1, o for faz isso automaticamente, conta do 0 até o tamanho final da lista
