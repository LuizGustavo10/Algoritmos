#
#
# def selectionSort(vetor):
#     print("--------------sua lista-----------------")
#     print(vetor)
#     print("------------ordenando lista-------------\n")
#
#
#     i = 0
#     while i < len(vetor) - 1: # a última posição do vetor não deve ser checada, o "i" não deve chegar a última posição, não é <=, é <
#
#         menor = i #guarda a posição, não o valor, é preciso a posição
#         j = i + 1 # o "j" smepre começa a frente o i, do "i" para tráz, ele não analisa
#
#         while j < len(vetor):
#             if vetor[j] < vetor[menor]: #analisa as posições e se "j" for menor, "j" assume a posição que tem o menor velor
#                 menor = j
#             j+=1
#         if menor != i: #se o menor estiver diferente de "i", ou seja se foi encontrado um valor menor que "i"
#             temp = vetor[i] #variável temporária guarda o vetor[i], para que o valor não se perda na troca de valores
#             vetor[i] = vetor[menor] #altera-se o vetor[i] para o menor valor
#             vetor[menor] = temp #e o vetor[menor] passa a ser a variável temporária
#         i+=1
#         print(vetor)
#     print("----------lista ordenada!----------------\n ")
#     print(vetor)
# vetor = [8,12,5,51,18]
# selectionSort(vetor)
#-------------------------------------------------------------
# #prova, praticar ação do algoritmo
# v = [8,12,5,51,18]
#
# 8 12 5 51 18
#
# 5 12 8 51 18
# 4 8 12 51 18
# 4 8 12 18 51
#
# 4 8 12 18 51
#
#
# pode cair o algoritmo buble, que troca menores para esqueda e maiores para direira


# forma de trocar os valores de A e B, sem variável:
# a= 10
# b = 7
# a = a - b       a = 10 - 7
# b = b - a       b = 7 - 10
# a = a + b       a = a + b

#------------------Algoritmo Bubble-------------------------
#gasta mais tempo

vetor = [7,4,2,9,18,1]
ordenado = False
while ordenado != True:

    ordenado = True
    j = 0
    while j < len(vetor) - 1:
        if vetor[j] > vetor[j+1]:
            temp = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = temp
            ordenado = False #verifica todo mundo, o ordenado é falso? Então inicia de novo a troca, caso contrario sai do laço
        j+=1
    print(vetor)

#treino nos dois exemplos
# 7,4,2,9,18,1    7,4,2,9,18,1
#
# 1,4,2,9,18,7    4,2,7,9,1,18
# 1,2,4,9,18,7    2,4,7,1,9,18
# 1,2,4,7,18,9    2,4,1,7,9,18
# 1,2,4,7,9,18    2,1,4,7,9,18
#                 1,2,4,7,9,18
# 1,2,4,7,9,18
#                 1,2,4,7,9,18
