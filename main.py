# main.py

import sys
import os

from CSVparser import *
from functions import *

# Lê o primeiro argumento na linha de comando como input
# e transforma dados em Packets
filename = sys.argv[1]
file = CSVparser(filename)
for i in file:
	Packet(i)

def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f'{len(Packets)} pacotes analisados com {len(PIDs.values())} PIDs diferentes')
	print('* * * * * * * * * * * * * * * * * * * * * * * * * *')
	print('menu() \t\t\t-> Retorna ao menu principal\n')
	print('plotPID(\"0x1F1\",\"1-8\")\t-> Gráfico dos bytes 1 a 8 do PID 0x1F1')
	print('\t\t\t   intervalos no formato \"1,4,6-8\"')
	print('\t\t\t   se o intervalo não for especificado retorna todos os bytes\n')
	print('print_Packets()\t\t-> Lista com todos os pacotes processados\n')
	print('PID_stats() \t\t-> Lista todos os PIDs e a frequencia deles\n')

menu()