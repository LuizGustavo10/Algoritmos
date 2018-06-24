# #1) Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
# #a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
# #b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
#
# lista = [""]*100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
#
# p = 0
# while p < len(lista):
#     print("Na posição {} tem o valor {}".format(p,lista[p]))
#     p+=1
#
# p = len(lista) - 1
# while p >= 0:
#     print("Na posição {} tem o valor {}".format(p,lista[p]))
#     p-=1

# # c) Mostre na tela o dobro de todos os números.------------------------------------------------------------------
# lista = [""]*100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
#
# p = 0
# while p < len(lista):
#     print("O dobro {} é {}".format(lista[p],lista[p]*2))
#     p+=1

#  #D) Apresente na tela a soma de todos os números.------------------------------------------------------------------
# lista = [""]*100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
# p = soma = 0
# while p < len(lista):
#     soma = soma + lista[p]
#     p+=1
# print("A soma total é {}".format(soma))

# #E) Apresente na tela a média geral dos valores contidos na lista.------------------------------------------------------------------
# lista = [""]*100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
# p = soma = 0
# while p < len(lista):
#     soma = soma + lista[p]
#     p+=1
# print("A média é {}".format(soma/len(lista)))

# #F) Mostre na tela a quantidade de números pares.------------------------------------------------------------------
# lista = [""]*100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
# p = par = 0
# while p < len(lista):
#     if lista[p] % 2 == 0:
#         par = par + 1
#     p+=1
# print("A quantidade de número pares é {}".format(par))

# #2)Faça um programa para armazenar 6 números inteiros para uma loteria, permitindo
# #que o usuário informe os números sorteados. Depois de preencher, informe uma mensagem e os números sorteados.--
# lista = [""]*6
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Insira o nº da para sortear: "))
#     p+=1
# p = 0
# print("Os nºs que vc jogou foram:")
# while p <len(lista):
#     print(lista[p], end=', ') #função end coloca o nº lado a lado
#     p+=1
# # 3)Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso. Faça um programa para armazenar
# # 5 nomes e permitir que o professor digite o nome da cada um. Em seguida, apresente na tela todos os nomes informados.
# lista = [""]*5
# p=0
# while p < len(lista):
#     lista[p] = input("Insira o nome do aluno: ")
#     p+=1
# p = 0
# print("O nome dos alunos cadastrados são: ")
# while p < len(lista):
#     print(lista[p])
#     p+=1
# # 4)Faça um programa que peça para o usuário informar o tamanho de um vetor. Em seguida, crie este vetor e
# # preencha ele com números digitados pelo usuário. Por fim, apresente na tela os números digitados.
# vetor = int(input("Insira o tamanho do vetor: "))
# lista = [""] * vetor
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Insira um nº: "))
#     p+=1
# p = 0
# print("Os nºs digitados foram")
# while p < len(lista):
#     print(lista[p])
#     p+=1
#5)-------------------------------------------------------------------------------------------------------
#a)Apresente os números do vetor em ordem inversa.
# vetor = int(input("Insira o tamanho do vetor: "))
# lista = [""]*vetor
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Insira um nº:"))
#     p+=1
# #^^^^^^Acima é a parte Universal^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]
# #ordem inversa
# p = len(lista) - 1
# print("Os números digitado em ordem inversa")
# while p >= 0:
#     print(lista[p],end =', ')
#     p-=1
# #B) apresente a soma de todos os elementos
# p = soma = 0
# while p < len(lista):
#     soma = soma + lista[p]
#     p+=1
# print("A soma total é",soma)
# #c) Calcule a média aritmética dos valores.
# p = soma = 0
# while p < len(lista):
#     soma = soma + lista[p]
#     p+=1
# print("A média aritmética é {}".format(soma/len(lista)))
# #D) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar os
# # números na tela. Por exemplo: na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 o usuário
# # teria que informar 4 e 8 (posição inicial e final, respectivamente) para mostrar na tela somente
# #  os valores destacados.
# print("A posição inicial é 0 até o maximo do vetor")
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final"))
# while p <= pf:
#     print("na posição {} tem o nº {}".format(p,lista[p]))
#     p+=1
# #E) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar a soma daquele
# # intervalo. Exemplo: Na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 , a soma do segmento destacado é 33.
#
# print("A posição inicial é 0 até o maximo do vetor")
# p = int(input("Insira a posição Inicial: "))
# pf = int(input("Insira a posição Final"))
# soma = 0
# while p <= pf:
#     print("na posição {} tem o nº {}".format(p,lista[p]))
#     soma = soma + lista[p]
#     p+=1
# print("A soma total é {}".format(soma))

# F) Encontre qual é o maior e o menor número desta lista. Além disso, informe quais são os índices (posições) deles.
# p = int(input("Insira a posição inicial: "))
# pf = int(input("Insira a posição final: "))
# maior = lista[p]
# menor = lista[p]
# par = impar = 0
# while p <= pf:
#     print("Na posição {} tem o valor {}".format(p,lista[p]))
#     if lista[p] > maior:
#         maior = lista[p]
#     if lista[p] < menor:
#         menor = lista[p]
#     if lista[p] % 2 == 0:
#         par +=1
#     else:
#         impar+=1
#     p+=1
# print("O maior nº é {} e o menor é {}".format(maior,menor))
# print("{} pares e {} impares".format(par,impar))
#  # 6)Crie um vetor para armazenar alguns números que serão utilizados no cálculo da tabuada.
#  # a) Apresente todos os números informados e seu respectivo dobro.
# vetor = int(input("Insira o vetor: "))
# lista = [""]*vetor
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Insira um nº:"))
#     p+=1
# p = 0
# while p < len(lista):
#     print("O dobro de {} é {}".format(lista[p],lista[p]*2))
#     p+=1
# #B)Para cada número presente no vetor, faça a tabuada do 1 ao 10 (utilizando laço de repetição).
# vetor = int(input("Insira o vetor: "))
# lista = [""]*vetor
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Insira um nº:"))
#     p+=1
# p = 0
#
# while p < len(lista):
#     tab = 0
#     while tab <= 10:
#         print("{}x{}={}".format(lista[p],tab,lista[p]*tab))
#         tab+=1
#     p+=1

# # 7) Um professor precisa armazenar uma lista de n alunos e seus respectivos conceitos. Crie um programa para auxiliar este professor.
# vetor = int(input("Insira a quantidade de aluno: "))
# listaAluno = ["palavra"]*vetor
# listaNota = [""]*vetor
# p = 0
# while p < len(listaAluno):
#     listaAluno[p] = input("Insira o nome do aluno: ")
#     listaNota[p] = int(input("Insira a nota do aluno: "))
#     p+=1
# p = 0
# while p < len(listaAluno):
#     print("O aluno {} tem a nota {}".format(listaAluno[p],listaNota[p]))
#     p+=1

# Usando um laço de repetição for
# for nomeDaVariavel in nomeDaLista:
# A variável escolhida vai assumir os valores da lista.
# A cada rodada ele assume o valor conforme a ordem que o vetor foi criado

# 8)Faça um programa para armazenar seis números inteiros para uma loteria, permitindo que
# o usuário informe os números sorteados. Em seguida, peça para o usuário informar os seis números que ele apostou.
# Por fim, apresente na tela quantos números ele acertou, informando se ele não ganhou nada (0 a 3 acertos),
# se acertou a quadra (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).
from random import randint

listaJogador = [""]*6
listaAleatoria = [""]*6
p = 0

while p < len(listaJogador):
    listaJogador[p] = int(input("Insira o número a ser jogado"))
    p+=1

x = 0
result = []
while x < len(listaAleatoria):
    listaAleatoria[x] = randint(1,60)
    if listaAleatoria[x] not in result:
        result.append(listaAleatoria[x])

    x+=1

#agora para comparar
acertos = p = 0
while p < len(listaJogador):

    x = 0
    while x < len(listaAleatoria):
        if listaJogador[p] == listaAleatoria[x]:
            acertos += 1
        x+=1
    p+=1
print("---------------------------------------------")
print("Nºs que você jogou {}".format(listaJogador))
print("Nºs que foram sorteados {}".format(listaAleatoria))
print("---------------------------------------------")

if acertos <= 3:
    print("você acertou {} nºs, não ganhou nada :(".format(acertos))
elif acertos == 4:
    print("você acertou {} nºs, ganhou a quadra".format(acertos))
elif acertos == 5:
    print("você acertou {} nºs, ganhou a quina".format(acertos))
elif acertos == 6:
    print("você acertou {} nºs, nunca mais vai precisar trabalhar :D".format(acertos))

# # 12) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# lista =["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
# listaResp = [""]*5
# p = 0
# print("digite 'S' para sim e 'N' para não.")
# while p < len(lista):
#     print(lista[p])
#     listaResp[p] = input("Sua resposta:")
#     p+=1
# p = pontos = 0
# while p < len(lista):
#     if listaResp[p] == "S" or listaResp[p] == "s":
#         pontos +=1
#     p+=1
# print(pontos)
# if pontos == 2:
#     print("Suspeito")
# elif pontos >= 2 and pontos <=3:
#     print("Cúmplice")
# elif pontos == 5:
#     print("Assassino!!!")
# else:
    # print("Inocente")

#13) Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:










# #10) Considerando que uma palavra (string) pode ser percorrida como um vetor,
# # faça um programa que peça o nome de uma pessoa e o apresente de trás para frente.
# palavra = input("Insira a palavra:")
# lista = ["palavra"]
#
# p = len(palavra) - 1
# while p >= 0:
#     print(palavra[p],end=", ")
#     p -= 1
