from random import randint
# option = 0
# lista = []
#
# while option != 4:
#     print('''
#     Escolha uma opção:
#     1 - cadastrar
#     2-ler
#     3-apagar e escrever
#     4-sair
#     ''')
#     option = int(input("Insira a opção: "))
#     if option == 1:
#         arquivo = open("arquivos/nomes.txt","a")
#         nome = str(input("Insira um nome: "))
#         arquivo.writelines(nome+"\n")
#         arquivo.close()
#     if option == 2:
#         arquivo = open("arquivos/nomes.txt","r")
#         conteudo = arquivo.readlines()
#         for x in range(0,len(conteudo)):
#             lista.append(conteudo[x])
#             print(lista[x])
#         arquivo.close()
#     if option == 3:
#         arquivo = open("arquivos/nomes.txt","w")
#         nome = input("insira o Nome: ")
#         arquivo.writelines(nome+"\n")
#         arquivo.close()
    # if option == 3:
    #
    # if option == 4:
    #     break


# # 12) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# lista =["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
# listaResp=[]
# cont = 0
# for x in range(0,len(lista)):
#     print("insira S para sim e N para não")
#     resp = input("Insira Sua Resposta: ").lower()
#
#     while resp != "s" and resp != "n":
#         print("ATENÇÃO: insira S para sim e N para não")
#         resp = input("Insira Sua Resposta").lower()
#
#     listaResp.append(resp)
#
#
#     if resp == "s":
#         cont+=1
#
# if cont == 1:
#     print("Ainda nada")
# if cont == 2:
#     print("Suspeita")
# if cont >=3 and cont <= 4:
#     print("Cumplice")
# if cont == 5:
#     print("assassino!!!")
# print(listaResp)
# print(cont)

# # Faça um programa para armazenar seis números inteiros para uma loteria, de modo que os seis números
# # sejam criados aleatoriamente pelo Python e que não sejam repetidos. Em seguida, peça para o usuário informar
# #  os seis números que ele apostou. Por fim, apresente na tela quantos números ele acertou, informando se ele não ganhou
# #  nada (0 a 3 acertos), se acertou a quadra (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar
# #   (6 acertos).
# listaLot=[]
# listaJog=[]
# acertos = 0
#
# while len(listaLot) < 6:
#     num = randint(0,60)
#
#     while num in listaLot:
#         num = randint(0,60)
#
#     listaLot.append(num)
# print(listaLot)
#
# while len(listaJog) < 6:
#     jog = int(input("Insira um nº: "))
#     while jog in listaJog:
#         jog = input("Você já jogou esse nº, insira outro!!!: ")
#     listaJog.append(jog)
#
#     for x in range(0, len(listaLot)):
#         if jog == listaLot[x]:
#             acertos += 1
# print(listaLot)
# print(listaJog)
# print(acertos)

# #-----------------------------------
# lista = ["Palavra"]
# teste = lista[0]
# for x in range(0,len(teste)):
#     print(teste[x])
