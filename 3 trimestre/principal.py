#coesão/complemento = muito importante

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
#menu Principal
    option = int(input("Insira uma opção: "))
    if option == 1:
        menu_contatos()
    elif option == 2:
        menu_usuario()

# Pelo que entendi, primeiro tem que ter uma parte de login que vai comparar
# com os cadastros de login do banco de dados, mostrando em seguida o menu principal
