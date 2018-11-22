from random import randint
# faz busca após estar ordenado
# compararar
# verificar se o elemento está em alguma posição no vetor
# # num = 3
# # 0 1 2 3 4 5
# f f f v f f análisa cada posição
#
# se está
# quantas vezes está na lista
# recursividade
vetor = [1,2,3,3,4,5]
n = 3

def buscar(vetor,n):

    for i in range(0,len(vetor)):
        print(i)
        if (i == n):
            return True
    return False


print(buscar(vetor,n))

print("---------------------------------------------")



def buscarNum(vetor,n):
    total = 0
    for i in range(0,len(vetor)):
        if vetor[i] == n:
            total+=1
        if vetor[i] > n and total > 0:
            return total
        print(vetor[i])


    return total

print(buscarNum(vetor,n))

# # busca binaria, busca pelo meio, busca pela metade, vai ter trabalho
# 0 a 50
# 0 a 25
#  12
#  18
#  15
#  13 ---resultado
#  6
#
#
# # recursividade - função chamando ela mesma
#
# 5!
# 4x3
# 3x2
# 2x1

# quando chegar a 1 a função vai parando


def somaRecursiva(vet,i):
    if i >= len(vet): #condição de oarada
        return 0 #finaliza a chamada e volta
    else: #faz uma nova chamada de função
        total = vet[1] + somaRecursiva(vet+1)
    return total
v = [1,2,3,4,5]
print(somaRecursiva(v,0))
