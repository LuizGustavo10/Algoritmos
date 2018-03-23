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
    print(" ")'''
#Construa um algoritmo, que receba três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
a = int(input("Insira um valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

if a>b>c:
    print(a, b, c)
elif b>a>c:
    print
