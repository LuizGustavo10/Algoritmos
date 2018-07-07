# from random import randint
# # Criação do vetor para armazenar números
# loteria = [""]*6
# # Variável de controle do laço de repetição
# i = 0
# # Laço para preencher o vetor
# while i < len(loteria):
#     # Gera número
#     num = randint(1,60)
#     # Variável para saber se repetiu ou não
#     repetiu = "n"
#
#     # Variável de controle do laço que verifica se o número já existe ou não
#     k = 0
#     # Laço para verificação do número
#     while k < i:
#         # Verifica se o núm está na posição k
#         if num == loteria[k]:
#             # Se for verdadeiro, o número já está lá
#             # Diminui o valor do "i" para fazer este processo novamente
#             i -= 1
#             # Muda o valor da variável repetiu
#             repetiu = "s"
#             # Parar o laço de repetição
#             break
#
#         # Incremento da posição
#         k += 1
#         # Fim do while do k
#
#     if repetiu == "n":
#         # Armazena
#         loteria[i] = num
#
#     # Incremento da posição
#     i += 1
#
# # Mostrar a lista gerada
# print(loteria)
#
# numeros = []
#
# while len(numeros) < 6
# num = randint(1,60)
# if num not in numeros:
#     numeros.append(num)
# print(numeros)
# vetor com varias palavras aleatorias
#desenhar as forkas
#usar o que a gente usou
#trabalhar com a gente viu
#iniciar desenhyo forka> sorteia a palavra e os risquinhos > usuário digita uma aleatorias
#verifica se tem a letra A e onde Determinar
# coloca A no risquinhos
#se não a cabeça do boneco
#lista dos que ja foram digitados, não pode repetir
#certa pode
#jogo com 7 erros morre, setimo erro morre
#você escolhe as palavras na lista, inicio do programa palavras = listadepalavras
# a cada erro vai ter um print ??????????
# |______
# |     |
# |     |
# |     0
# |     /\\ coloque os braços de duas barras para dar certo
# |
# |
#palavras = [
# "ifpr",
# "Cachorros",
# "mundial"
# ]
#dicas = [
# "É uma instituição de ensino"
# ]
# É par ao dia 12, não deixe para ultima hora
#num =3
#print(palavra[3])
#print(dica[3])
#várias lista, lista das letras que foram digitadas
# vetor vazio [], cada vez que digita uma letra aumenta o vetor, append pode usar
# letrasDigitadas.append letra
# riscos = ["_"]*10, para 10 posições de palavra


# print("""
#
# """)
# #Exemplo de Forca abaixo
# palavraSecreta = ["L","U","I","Z"]
# letrasDescobertas = []
#
# print("---------Jogo da Forca----------")
#
# for i in range(0, len(palavraSecreta)):  #é como se fosse o p = p + 1, vai até o tamanho da palavra
#     letrasDescobertas.append("_") #coloca o tracinho no lugar de cada letra
#
# acertou = False
#
# while acertou == False: #Enquanto ele não acertou
#     letra = input("dígite a letra: ")
#
#     for i in range(0, len(palavraSecreta)): #percorre cada uma das letras da palavraSecreta, para verificar se a letra é correta
#         if letra == palavraSecreta[i]: #compara a cada uma das letras de palavra secreta
#             letrasDescobertas[i].append(letra) #substitui o tracinho pela letra
#
#         print(letrasDescobertas[i])
#
#     acertou = True #abaixo vai verificar as letras que foram descobertas
#     for p in range(0, len(letrasDescobertas)):
#         if letrasDescobertas[p] == "_":
#             acertou = False

#funções

# estudar funções
#inicio
def mostrarErro1():
    # mostrar/pedir numeros, sempre use um verbo no
    print("Oloco")

    # seu códifo lá em baixo:
erro=1

if erro == 1:
    mostrarErro1()
