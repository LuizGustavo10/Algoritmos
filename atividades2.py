#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''print("----------------------Questão 01 --------------------")
numero = int(input("Digite um número: "))
if numero > 0:
    print(numero,"é um número positivo")
elif numero < 0:
    print(numero, "é um número negativo")
else:
    print(numero, "é um número neutro")
print(" ")

#Faça um Programa que peça dois números e imprima o maior deles.
print("----------------------Questão 02 --------------------")
primeiroN = int(input("Insira o primeiro número: "))
segundoN = int(input("Insira o segundo número: "))

if primeiroN > segundoN:
    print("O primeiro Número é maior")
elif segundoN > primeiroN:
    print("O segundo número é maior")
else:
    print("Os números são iguais")
print(" ")
#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
print("----------------------Questão 03 --------------------")

a = int(input("Insira o valor de A"))
b = int(input("Insira o valor de B"))
c = int(input("Insira o valor de C"))

if a+b < c:
    print(a, "+", b,"é menor que", c)
elif a+b > c:
    print(a, "+", b,"é maior que", c)
else:
    print(a, "+", b,"é igual a", c)
#Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
print("----------------------Questão 04 --------------------")
sexo = input("Insira M para masculino, F para feminino")
if sexo == "M" or sexo == "m":
    print("M - masculino")
elif sexo == "F" or sexo == "f":
    print("F - feminino")
else:
    print("Caracter inválido")
print(" ")
#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
print("----------------------Questão 05 --------------------")
numero = int(input("Insira um número: "))
if numero %2 == 0:
    print("O número é par")
else:
    print("O número é impar")
print(" ")
#Faça um algoritmo que leia um número e some 5 caso seja par ou some 8 caso seja ímpar. Por fim, imprima o resultado desta soma.
print("----------------------Questão 06 --------------------")
numero = int(input("Insira um número: "))
if numero %2 == 0:
    numero = numero + 5
    print(numero)
else:
    numero = numero + 8
    print(numero)
print(" ")
#Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
print("----------------------Questão 07 --------------------")
trab = int(input("Insira a nota do trabalho: "))
prova = int(input("Insira a nota da prova: "))
if trab+prova>=60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
    print(" ")
#Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
print("----------------------Questão 08 --------------------")
a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))


if a > b and a > c:
    print(a,"que representa A é o maior número")
elif b > a and b > c:
    print(b,"que representa B é o maior número")
elif c > a and c > b:
    print(c,"que representa C é o maior número")
else:
    print("Os números são iguais")


#Construa um algoritmo, que receba três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
print("--------------Questão 09-------------------")
a = int(input("Insira um valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

if a>b>c:
    print(a,b,c)

elif (a>c>b):
    print(a,c,b)

elif(b>a>c):
    print(b,a,c)

elif(b>c>a):
    print(b,c,a)

elif(c>a>b):
    print(c,a,b)

elif(c>b>a):
    print(c,b,a)
else:
    print("Há algo errado")
#Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente as funções necessárias:
#10 questão atividades 2
print("--------------Questão 10-------------------")
print("== Menu de opções ==") #menu de opção
print("1. Somar 2 números")
print("2. Potência de um número")
print("3. Raiz de grau N")
option = int(input("== Opção escolhida: "))
print("--------------------------")

if option == 1:
    print("Opção soma escolhida!")
    primeiroN = int(input("Insira o primeiro número: "))
    segundoN = int(input("Insira o segundo número: "))
    total = primeiroN + segundoN
    print(primeiroN, "+", segundoN, "=", total)
elif option == 2:
    print("Opção potenciação escolhida!")
    numero = int(input("Escolha algum número: "))
    potencia = int(input("Escolha a potência a ser elevada: "))
    total = numero ** potencia
    print(numero,"elevado a ", potencia,"=", total)
elif option == 3:
    print("Opção raiz escolhida!")
    numero = int(input("Insira algum número: "))
    raiz = int(input("Insira o tipo de raiz: "))
    total = numero ** (1/raiz)
    print("A raiz", raiz, "do nº", numero, "=", total)
else:
    print("opção inválida")
# questão 11
print("----------------Questão 11---------------------")
preco = float(input("Insira o preço do produto: "))
d10 = preco * (10/100)
precoFinal = preco - d10
print("Desconte de R$", d10)
print("O preço total após o desconto de 10% é: R$",precoFinal)
#Questão 121
print("--------------Questão 12----------------")
salarioBruto = float(input("Insira seu salário total: "))
print("Salário Bruto: R$",salarioBruto)

if salarioBruto > 3000:
    imposto = salarioBruto * (15/100)
    print("O imposto é equivale a R$", imposto)
    print("Seu salário líquido é R$", salarioBruto - imposto)
elif salarioBruto < 3000:
    imposto = salarioBruto * (7.5/100)
    print("O imposto é equivalente a R$", imposto)
    print("Seu salário líquido é R$", salarioBruto - imposto)
else:
    print("Ops... Algo deu errado")
#Questão 13
print("------------------Questão 13------------------------")
a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))
d = int(input("Insira o quarto número: "))
# o maior
if a>c and a>b and a>d:
    print("O maior nº é", a)
elif b>a and b>c and b>d:
    print("O maior nº é", b)
elif c>a and c>b and c>d:
    print("O maior nº é", c)
elif d>a and d>b and d>c:
    print("O maior nº é", d)
else:
    print("Os números são iguais")

    # o menor
if a<b and a<c and a<d:
    print("O menor nº é", a)
elif b<a and b<c and b<d:
    print("O menor nº é", b)
elif c<a and c<b and c<d:
    print("O menor nº é", c)
elif d<a and d<b and d<c:
    print("O menor nº é", d)
else:
    print("Os números são iguais")

#Questão 14
print("---------------------Questão 14--------------------------")
x = int(input("Insira o valor de X: "))

if x < 2:
    result = 1/(2-x)
elif x >= 2:
    result = 1/(x-2)
else:
    print("operação não suportada")

print("O resultado é",result)

#Questão 15
print("---------------------Questão 15--------------------------")
altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(imc)
    print("Classificado com baixo peso")

elif imc > 18.5 and imc < 24.9:
    print(imc)
    print("Classificado como peso normal")

elif imc > 25 and imc < 29.9:
    print(imc)
    print("Classificado como pré obesidade")

elif imc > 30 and imc < 34.9:
    print(imc)
    print("Classificado como obesidade grau 1")

elif imc > 35 and imc < 39.9:
    print(imc)
    print("Classificado como obesidade grau 2")

elif imc > 40:
    print(imc)
    print("Classificado como obesidade grau 3")
else:
    print("Não suportado")
#Questão 16
print("---------------------Questão 16--------------------------")
salario = float(input("Insira seu salário para o reajuste: "))
print("Salário antes do reajuste: R$",salario)

if salario <= 710:
    print("Aumento de 20%")
    aumento = salario * (20/100)
    salarioFinal = salario + aumento
    print("O aumento equivale a R$", aumento)

elif salario > 710 and salario <=1000:
    print("Aumento de 15%")
    aumento = salario * (15/100)
    salarioFinal = salario + aumento
    print("O aumento equivale a R$", aumento)

elif salario > 1000 and salario <=2500:
    print("Aumento de 10%")
    aumento = salario * (10/100)
    salarioFinal = salario + aumento
    print("O aumento equivale a R$", aumento)
elif salario > 2500:
    print("Aumento de 5%")
    aumento = salario * (5/100)
    salarioFinal = salario + aumento
    print("O aumento equivale a R$", aumento)
else:
    print("valor inválido")

print("O salário final após o aumento é R$",salarioFinal)'''
#Questão 17
print("---------------------Questão 17--------------------------")
morango = float(input("Insira a quantidade em KG de morangos: "))
maca = float(input("Insira a quantidade em KG de maçãs: "))

if morango >= 5 or maca >= 5:

    elif morango > 5 or maca > 5:
