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
# # c) Mostre na tela o dobro de todos os números.
#
# lista = [""]*100
# listaDobro = [""]*100
# p = 0
# n = 1
# dobro = 1
# while p < len(lista):
#     lista[p] = n
#     listaDobro[p] = lista[p] * 2
#     n+=1
#     p += 1
#
# p = 0
# while p < len(lista):
#     print("na posição", p, " - valor", lista[p])
#     print("O seu dobro é", listaDobro[p])
#     print("---------------------------------------")
#     p+=1
#
# #D) Apresente na tela a soma de todos os números.
#
# lista = [""]*100
#
# p = soma = 0
# n = 1
# dobro = 1
# while p < len(lista):
#     lista[p] = n
#     soma = soma + lista[p]
#     n+=1
#     p += 1
#
# p = 0
# while p < len(lista):
#     print("na posição", p, " - valor", lista[p])
#     print("---------------------------------------")
#     p+=1
# print("A soma de todos os números é", soma)

# #E) Apresente na tela a média geral dos valores contidos na lista.
#
# lista = [""]*100
#
# p = soma = 0
# n = 1
# dobro = 1
# while p < len(lista):
#     lista[p] = n
#     soma = soma + lista[p]
#     n+=1
#     p += 1
#
# p = 0
# while p < len(lista):
#     p+=1
# print("A media é", soma/len(lista))

# #F) Mostre na tela a quantidade de números pares.
#
# lista = [""]*100
#
# p = soma = par = 0
# n = 1
# dobro = 1
# while p < len(lista):
#     lista[p] = n
#     if lista[p] % 2 == 0:
#         par += 1
#     n+=1
#     p += 1
#
# print(par, "nºs pares")
#
#
#

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

# # 3)Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso. Faça um programa para armazenar
# # 5 nomes e permitir que o professor digite o nome da cada um. Em seguida, apresente na tela todos os nomes informados.
# lista = [""]*5
# p = 0
# while p < len(lista):
#     lista[p] = str(input("Insira o seu nome:"))
#     p+=1
#
# p=0
# print("------------------------")
# print("Os nomes dos aluno são:")
# while p < len(lista):
#     print(lista[p])
#     p+=1

# # 4)Faça um programa que peça para o usuário informar o tamanho de um vetor. Em seguida, crie este vetor e
# # preencha ele com números digitados pelo usuário. Por fim, apresente na tela os números digitados.
#
# vetor = int(input("Insira o tamanho do vetor: "))
# lista = [""]* vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número: "))
#     p+=1
#
# print("-----------------------------")
# p= 0
# while p < len(lista):
#     print("Você digitou: ",lista[p])
#     p+=1

# #5)
# #a)Apresente os números do vetor em ordem inversa.
# vetor = int(input("Insira o tamanho do vetor: "))
# lista = [""]* vetor
# p = len(lista) - 1
#
# while p >= 0:
#     lista[p] = int(input("Agora digite um número: "))
#     p-=1
#
# print("-----------------------------")
# p= 0
# while p < len(lista):
#     print("Você digitou: ",lista[p])
#     p+=1


# #B) Apresente a soma de todos os elementos.
# vetor = int(input("Insira o tamanho do vetor: "))
# lista = [""]* vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número: "))
#     p+=1
#
# print("-----------------------------")
# soma = 0
# p = 0
# while p < len(lista):
#     soma += lista[p]
#     p += 1
# print("A soma total é",soma)
# #c) Calcule a média aritmética dos valores.
# vetor = int(input("Insira o tamanho do vetor: "))
# lista = [""]* vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número: "))
#     p+=1
#
# print("-----------------------------")
# soma = 0
# p = 0
# while p < len(lista):
#     soma += lista[p]
#     p += 1
# print("a média é",soma/len(lista

# #D) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar os
# # números na tela. Por exemplo: na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 o usuário
# # teria que informar 4 e 8 (posição inicial e final, respectivamente) para mostrar na tela somente
# #  os valores destacados.
# vetor = int(input("Insira o tamanho do vetor: "))
# print("------------------------------------------")
#
# lista = [""]*vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número"))
#     p += 1
#
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final: "))
#
# while p <= pf:
#     print("na posição",p," - valor",lista[p])
#     p += 1

# #E) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar a soma daquele
# # intervalo. Exemplo: Na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 , a soma do segmento destacado é 33.
#
# vetor = int(input("Insira o tamanho do vetor: "))
# print("------------------------------------------")
#
# lista = [""]*vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número"))
#     p += 1
#
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final: "))
# soma = 0
#
# while p <= pf:
#     print("na posição",p," - valor",lista[p])
#     soma += lista[p]
#     p += 1
#
# print("A soma total é", soma)

# # F) Encontre qual é o maior e o menor número desta lista. Além disso, informe quais são os índices (posições) deles.
# vetor = int(input("Insira o tamanho do vetor: "))
# print("------------------------------------------")
#
# lista = [""]*vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número"))
#     p += 1
# print("------------------------------------------")
# print("Lembrando que a posição começa em 0")
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final: "))
#
# maior = lista[p]
# menor = lista[p]
#
# while p <= pf:
#     print("na posição",p," - valor",lista[p])
#     if lista[p] > maior:
#         maior = lista[p]
#     if lista[p] < menor:
#         menor = lista[p]
#     p += 1
# print("------------------------------------------")
# print("O maior número é",maior)
# print("O menor número é",menor)

# #G)Encontre qual é o maior e o menor número desta lista. Além disso, informe quais são os índices (posições) deles.
# vetor = int(input("Insira o tamanho do vetor: "))
# print("------------------------------------------")
#
# lista = [""]*vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número"))
#     p += 1
# print("------------------------------------------")
# print("Lembrando que a posição começa em 0")
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final: "))
#
# maior = lista[p]
# menor = lista[p]
# posicaoA = p
# posicaoB = p
#
# while p <= pf:
#     print("na posição",p," - valor",lista[p])
#     if lista[p] > maior:
#         maior = lista[p]
#         posicaoA = p
#     if lista[p] < menor:
#         menor = lista[p]
#         posicaoB = p
#     p += 1
# print("------------------------------------------")
# print("O maior número é",maior,"e está na posição", posicaoA)
# print("O menor número é",menor,"e está na posição", posicaoB)

# # H) Informe quantos números pares e ímpares foram digitados (apenas a quantidade de cada).
# vetor = int(input("Insira o tamanho do vetor: "))
# print("------------------------------------------")
#
# lista = [""]*vetor
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Agora digite um número"))
#     p += 1
# print("------------------------------------------")
# print("Lembrando que a posição começa em 0")
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final: "))
# par = impar = 0
#
# while p <= pf:
#     print("na posição",p," - valor",lista[p])
#     if lista[p] % 2 == 0:
#         par += 1
#     else:
#         impar +=1
#     p += 1
#
# print("------------------------------------------")
# print("A quantida de número(s) par é",par)
# print("A quantida de número(s) impar é",impar)

# # 6)Crie um vetor para armazenar alguns números que serão utilizados no cálculo da tabuada.
# # a) Apresente todos os números informados e seu respectivo dobro.
# vetor = int(input("Insira o tamnho da lista de números:"))
# lista = [""]*vetor
#
# p = 0
# print("------------------------------------------")
# while p < len(lista):
#     lista[p] = int(input("Insira o número:"))
#     p+=1
#
# p = 0
# print("------------------------------------------")
# while p < len(lista):
#     print("O número digitado foi",lista[p]," e seu dobro é",2*lista[p])
#     p+=1

# #B)Para cada número presente no vetor, faça a tabuada do 1 ao 10 (utilizando laço de repetição).
# vetor = int(input("Insira o tamanho da lista de números:"))
# lista = [""]*vetor
#
# p = 0
# print("------------------------------------------")
# while p < len(lista):
#     lista[p] = int(input("Insira o número"))
#     p+=1
#
# p = 0
# print("------------------------------------------")
# while p < len(lista):
#     tab = 0
#     print("Tabuado do número",lista[p])
#     while tab <= 10:
#         print(lista[p],"x",tab,"=",lista[p]*tab)
#         tab+=1
#     print("-----------------------------------------")
#     p += 1

# 7) Um professor precisa armazenar uma lista de n alunos e seus respectivos conceitos. Crie um programa para auxiliar este professor.
vetor = int(input("Insira a quantidade de alunos"))
listaAluno = [""]*vetor
listaNota = [""]*vetor
p= 0

while p < len(listaAluno):
    listaAluno[p] = str(input("Insira o nome do Aluno: "))
    listaNota[p] = int(input("Insira a nota do Aluno: "))
    print("------------------------------")
    p+=1

p= 0
while p < len(listaAluno):
    print("nome:",listaAluno[p])
    print("nota:",listaNota[p])
    p+=1
    print("-------------------------------")
