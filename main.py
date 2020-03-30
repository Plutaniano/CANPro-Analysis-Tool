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

os.system('cls' if os.name == 'nt' else 'clear')
print('* * * * * * * * * * * * * * * * * * * * * * * * * *')
print('getPIDstats() \t\t-> Lista todos os PIDs e a frequencia deles')
print('plotPID(\"0x1F1\",\"1-8\")\t-> Gráfico dos bytes 1 a 8 do PID 0x1F1')
print('Packets \t\t-> Lista com todos os pacotes processados')
print('PIDs \t \t \t-> Dicionário com todos os PIDs processados')
