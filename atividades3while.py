
# #1)a) Apresente na tela os números de 1 a 100.
# print("-------------Questão 01-A------------------------------------------------------")
# n = 1
# while n<=100:
#     print(n)
#     n+=1
# print("Fim do programa")
# print("-------------Questão 01-B------------------------------------------------------")
# #1)b) Faça a soma dos números de 1 a 100 e apresente somente o resultado.
# n = 1
# nantigo = 0
# while n <=100:
#     print(n)
#     nantigo +=n
#     n +=1
# print(nantigo)
# print("-------------Questão 01-C------------------------------------------------------")
# #1)c) Apresente na tela somente os números pares entre 1 e 100.
# n = 1
# while n <=100:
#     if n % 2 == 0:
#         print(n)
#     n += 1
# print("-------------Questão 01-D------------------------------------------------------")
# #1) d)Apresente na tela somente a soma dos números pares entre 1 e 100.
# n = 1
# total = 0
# while n<=100:
#     if n % 2 == 0:
#         #print(n)
#         total += n
#     n += 1
# print(total)
#
# print("-------------Questão 01-E------------------------------------------------------")
# #1) e) Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e de Y).
# x = int(input("Insira o valor inicial de x: "))
# y = int(input("Insira o valor final de y: "))
#
# while x>y:
#     print("O valor inicial é maior que o valor final, Por favor, digite novamente...")
#     x = int(input("Insira o valor inicial de x: "))
#     y = int(input("Insira o valor final de y: "))
#
# while x <= y:
#     print(x)
#     x+=1
# print("Fim do programa")
#
# print("-------------Questão 01-F------------------------------------------------------")
# #f) Faça a soma dos números de X a Y e apresente somente o resultado (peça para o usuário informar os valores de X e de Y).
# x = int(input("insira o valor inicial de X: "))
# y = int(input("Insira o valor final de Y: "))
# soma = 0
#
# while x > y:
#     print("O valor inicial é maior que o valor final, Por favor, digite novamente...")
#     x = int(input("insira o valor inicial de X: "))
#     y = int(input("Insira o valor final de Y: "))
# while x <= y:
#     print(x)
#     soma += x
#     x += 1
# print(soma)
#
# print("-------------Questão 01-G------------------------------------------------------")
# #g) Apresente na tela somente os números ímpares entre X e Y (peça para o usuário informar os valores de X e de Y).
# x = int(input("Insira o valor inicial de X: "))
# y = int(input("Insira o valor final de Y: "))
#
# while x > y:
#     print("O valor inicial é maior que o valor final, Por favor, digite novamente...")
#     x = int(input("Insira o valor inicial de X: "))
#     y = int(input("Insira o valor final de Y: "))
# while x <= y:
#     if x % 2 != 0:
#         print(x)
#     x+=1

# # 2) Faça um programa para calcular a tabuada:
# print("-------------Questão 02-A------------------------------------------------------")
# # 2) A) do 1 ao 10 para um número informado pelo usuário.
# n = int(input("Insira um nº para calcular a tabuada de 1 ao 10: "))
# tabuada = 0
# while tabuada <= 10:
#     result = n * tabuada
#     print(n,"x",tabuada,"=",result)
#     tabuada += 1
#
# 2) B) do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).
# print("-------------Questão 02-B------------------------------------------------------")
# n = int(input("Insira um nº para calcular a tabuada: "))
# x = int(input("Insira o valor inicial de X de multiplicação: "))
# y = int(input("Insira o valor final de Y de multiplicação: "))
#
# while x > y:
#     print("O valor inicial é maior que o valor final, por favor, dígite novamente")
#     x = int(input("Insira o valor inicial de X de multiplicação: "))
#     y = int(input("Insira o valor final de Y de multiplicação: "))
#
# while x <= y:
#     result = n * x
#     print(n,"X",x,"=",result)
#     x += 1
# print("-------------Questão 03-------------------------------------------------------")
# #3) Na matemática, o fatorial de um número natural n, representado por n!, é o produto de todos os
# # inteiros positivos menores ou iguais a n. Por exemplo: o fatorial de 5 é representado por 5! que é igual a
# # 5 x 4 x 3 x 2 x 1. Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.
# n = int(input("Insira um número para ser calculado o fatorial: "))
# f = 1
# exemplo = n
# while n != 0:
#     print(n)
#     f = f * n
#     n-=1
# # print(exemplo,"! =",f)
# print("-------------Questão 04-------------------------------------------------------")
# #----menu-----------
#
# option = 0
#
# while option != 4:
#     print('''====== Menu Principal ======
#     1. Par ou ímpar?
#     2. Potência XY
#     3. Raiz quadrada
#     4. Sair
# ============================''')
#     option = int(input("Qual a sua opção? "))
#     print("============================")
#
#     if option == 1:
#         n = int(input("Insira um número: "))
#         if n % 2 == 0:
#             print(n,"é um número par")
#         else:
#             print(n,"é um número impar")
#     elif option == 2:
#         n = int(input("Insira o valor da base: "))
#         potencia = int(input("Insira a nº elevado: "))
#         total = n ** potencia
#         print(total)
#     elif option == 3:
#         n = int(input("Insira um nº para ser calculado a raiz: "))
#         print("A raiz de ",n,"é", n ** (1/2))
#     elif option == 4:
#         print("Saindo...")
#     else:
#         print("opção inválida, porfavor, escolha novamente: ")
#
# print("Fim do programa, volte sempre!")
#
# print("-------------Questão 05-------------------------------------------------------")
# #----menu-----------
# option = 0
#
# while option != 4:
#     print('''====== Menu Principal ======
# 1. Fazer a tabuada do 1 ao 10 para um número X
# 2. Apresentar os múltiplos de X entre 1 e 100
# 3. Apresentar a soma dos números de 1 a 100
# 4. Sair do programa''')
#     print("============================")
#     option = int(input("Qual a sua opção?"))
#     print("============================")
    # if option == 1:
        # x = int(input("Insira um número para a tabuada: "))
        # n=1
        # while n <=10:
        #     total = x * n
        #     print(x,"X",n,"=",total)
        #     n+=1
#     elif option == 2:
#         n = int(input("Insira um número para achar seus múltiplos: "))
#         teste = 0
#         while teste<=100:
#             if teste % n == 0:
#                 print(teste)
#             teste+=1
#     elif option == 3:
#         n = 1
#         soma = 0
#         while n<=100:
#             soma+=n
#             n+=1
#         print(soma)
#     elif option == 4:
#         print("Saindo...")
#     else:
#         print("opção inválida, porfavor tente novamente")
# print("Fim do programa, volte sempre!")
#("-------------Questão 06-------------------------------------------------------")
# print("-------------Questão 06-------------------------------------------------------")
# n = 1
# soma = 0
# while n != 0:
#     print("Para o final da compra dígite 0 ")
#     n = float(input("Insira o valor do produto: "))
#     soma += n
# print("O total é R$",soma)
# rsCliente = float(input("Quanto de dinheiro cliente forneceu? "))
# print("O troco é R$", rsCliente - soma)

# #("-------------Questão 07-------------------------------------------------------")
# resp = "s"
# quantidade = 0
# maior = 0
# menor = 0
# soma = 0
# temp = 0
#
# while resp in "Ss":
#     temp = int(input("Insira o valor da temperatura:"))
#     soma += temp
#     quantidade += 1
#     if quantidade == 1:
#         maior = temp
#         menor = temp
#     else:
#         if temp > maior:
#             maior = temp
#         if temp < menor:
#             menor = temp
#
#     resp = str(input("Quer continuar [S/N]"))
#
# print("A média de temperatura é",(soma/quantidade))
# print("A maior temperatura é ", maior)
# print("A menor temperatura é ", menor)
# print("-------------Questão 08-------------------------------------------------------")
# nota = quantidade = soma = 0
# nota = int(input("Insira sua nota"))
# while nota != -1:
#     quantidade +=1
#     soma += nota
#     nota = int(input("Insira sua nota"))
# print("Sua média é",soma/quantidade)
# print(quantidade)
# print("-------------Questão 08 - método 2---------------------------------------------")
# nota = quantidade = soma = 0
# while nota != -1:
#     nota = int(input("Insira sua nota"))
#     if nota == -1:
#         break
#     soma += nota
#     quantidade +=1
# print("Sua média é",soma/quantidade)
# print(quantidade)
#
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e
# o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
# print("-------------Questão 09-------------------------------------------------------")
# quantidade = int(input("Insira a quantidade de CDs que foram adquiridos:"))
# n=1
# total=0
#
# while n <= quantidade:
#     valor = int(input("Insira o Valor de seu novo CD: "))
#     total += valor
#     n += 1
# print("O total ivestido foi R$", total)
# print("O valor médio gasto em cada CD é R$",total/quantidade)

# print("-------------Questão 10-------------------------------------------------------")
quantidade = codigo = 1
maiorP = menorP = maiorA = menorA = codMaiorA = codMenorA = codMaiorP = codMenorP =  mediaA = mediaP = 0
codigo = int(input("Insira seu código"))
altura = float(input("Insira sua altura"))
peso = float(input("Insira seu peso"))

while codigo != 0:
    if quantidade == 1:
        maiorA = altura
        menorA = altura
        maiorP = peso
        menorP = peso
        codMaiorA = codigo
        codMenorA = codigo
        codMaiorP = codigo
        codMenorP = codigo
        mediaA = altura
        mediaP = peso

    codigo = int(input("Insira seu código"))
    if codigo == 0:
        break
    altura = float(input("Insira sua altura"))
    peso = float(input("Insira seu peso"))

    mediaA += altura
    mediaP += peso

    if altura > maiorA:
        maiorA = altura
        codMaiorA = codigo
    if altura < menorA:
        menorA = altura
        codMenorA = codigo
    if peso > maiorP:
        maiorP = peso
        codMaiorP = codigo
    if peso < menorP:
        menorP = peso
        codMenorP = codigo


    quantidade +=1
totA = mediaA / quantidade
totP = mediaP / quantidade

print("A maior altura é", maiorA,"- Código cliente =", codMaiorA)
print("A menor altura é", menorA,"- Código cliente =", codMenorA)
print("O maior peso é", maiorP,"- Código cliente =", codMaiorP)
print("O menor peso é", menorP,"- Código cliente =", codMenorP)
print("A média de altura é", totA)
print("A média de peso é", totP)

# print("-------------Questão 11-------------------------------------------------------")
# base = int(input("Insira o valor final da base da fração: "))
# total = 0
# cont = 1
#
# while cont <= base:
#     total += (1/cont)
#     cont +=1
# print("O total do valor de H é", total)

# print("-------------Questão 12-------------------------------------------------------")
# maiorNota = menorNota = contador = 1
# soma = 0
# nome = str(input("Insira o nome do atleta: "))
# while contador <= 7:
#     notas = int(input("Insira a nota: "))
#     if notas > maiorNota:
#         maiorNota = notas
#     if notas < menorNota:
#         menorNota = notas
#     print(contador)
#     soma+=notas
#     contador+=1
# total = soma - maiorNota - menorNota
# print("Resultado final")
# print("Atleta",nome)
# print("Maior Nota =",maiorNota)
# print("Menor Nota =",menorNota)
# print("A média é",total/5)

# # 13) Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e
# # que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e apresente
# # o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
# # de crescimento de cada um.
# a = 80000
# b=200000
# ano=0
# while a <= b:
#     aumentoA = a * (3/100)
#     a+=aumentoA
#     aumentoB = b * (1.5/100)
#     b+=aumentoB
#     ano+=1
# print(ano,"anos")
# print(a)
# print(b)









#
