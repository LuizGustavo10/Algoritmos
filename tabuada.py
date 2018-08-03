# def multiplicar():
#     n = int(input("Insira o nº para calcular a tabuada: "))
#     for x in range(0,11):
#         print("{} x {} = {}".format(n,x,n*x))
# #-------------------------------------------------------------------------------
# multiplicar()
# def exemplo2(num):
#     if (num % 2 == 0):
#         print("O número é par!")
#     else:
#         print("O número é impar!")
#
# a = int(input("Insira o nº: "))
# exemplo2(a)
# #-------------------------------------------------------------------------------
#
# def multiplicar(n):
#     for x in range(0,11):
#         print("{} x {} = {}".format(n,x,n*x))
#
# n = int(input("Insira o nº para calcular a tabuada: "))
# multiplicar(n)
# ##python diferencia um mesmo perâmetro, por exemplo  multiplicar multiplicar(n) multiplicar(z)
# #-------------------trabalhando com valor de retorno-----------------------------------
def exemplo4(num):
    if num % 2 == 0:
        return num**2
    else:
        n = num ** 3
        return n
k = exemplo4(3)
print("Resultado = ",k)
print(k * 3)
