# main.py

from classes import *
from CSVparser import *
from funcoes import *
import sys

# Lê o primeiro argumento na linha de comando como input
# e transforma dados em Packets
filename = sys.argv[1]
file = CSVparser(filename)
for i in file:
	Packet(i)

getPIDstats()