# importações
import os #funções do S.O
import sqlite3 # Importa a biblioteca sqlite
import sys

# CORES
verde = '\033[01;32m'
vermelho = '\033[01;31m'
amarelo = '\033[93m'
cyan = '\033[96m'
cyanesc = '\033[36m'
nativa = '\033[m'
negrito = '\033[1m'
sys.stdout.write(nativa)

def tracejado_verde():
    print("\033[1;32m"+"------------------------------------"+"\033[m")
