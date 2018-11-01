-------------ORDENAÇÂO------------------------------------
--------- Algoritmo selection sort------------------------

melhor caso = crescente
1 2 3 4 6                = economiza computação, de valor tal a tal
caso medio = o maior numero de possibilidades
3 2 1 4 6
pior caso = decrescente
10 9 8 4 3

Exemplo, voce busca varios salarios, e busca tal valor a tal, para não gastar processamento com outros registros

quanto menos tempo melhor na quantidade de dados


ele organiza o vetor, comparando com o valor da frente e assim por diante, bem parecido com o que foi feito na forca

4 3 2 -1 7 9 nums = v
0 1 2  3 4 5 posições
i j

"J" = i + 1 , percorre o vetor, posição "J"
"i" = menor
tudo se organiza pelas posições
-------------------------------------------------------------
if v[j] < v[menor]
menor é uma posição
menor = j

i fica no 0
o J percorre a lista, quando encontra o menor -1, ele deixa marcado como o valor menor em certa posição exempo = "-1"

novo resultado
-1 3 2 4 7 9 nums = v
0  1 2 3 4 5 posições

próximo resultado

-1 2 3 4 7 9

como funciona a troca de números
"C" é uma variável temporária
a = 3 b = 5
c = a
a = b
a = c
