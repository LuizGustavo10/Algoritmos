# #1) Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
# #a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
# #b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
#
# lista = [""]*100
# p = 0
# n = 1
# while p < len(lista):
#     lista[p] = n
#     n+=1
#     p += 1
#
# p = 0
# while p < len(lista):
#     print("na posição", p, " - valor", lista[p])
#     p+=1
#
# print("Inversamente temos --------------------------------------")
#
# p = len(lista) - 1
#
# while p >= 0:
#     print("na posição", p," - valor", lista[p])
#     p-=1

# #2)Faça um programa para armazenar 6 números inteiros para uma loteria, permitindo
# #que o usuário informe os números sorteados. Depois de preencher, informe uma mensagem e os números sorteados.
# lista = [""]*6
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Insira um número para a loteria: "))
#     p+=1
#
# p = 0
# print("os números que você jogou foram")
# while p < len(lista):
#     print(lista[p], end=', ') # função end coloca os nºs lado a lado
#     p+=1
