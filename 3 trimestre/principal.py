from usuario import *
from outros import *
from contato import *


option = 10
while option != 0:
    print('''\033[1;36m
----------Menu Principal-----------+
1 - Contatos                       |
2 - Usuário                        |
0 - Sair                           |
-----------------------------------+\033[m''')
    option = int(input("Insira uma opção: "))
    if option == 1:
        menu_contatos()
    elif option == 2:
        menu_usuario()
