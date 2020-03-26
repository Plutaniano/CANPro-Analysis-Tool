# txt2csv.py
# script simples para transformar dados do CANPro de .txt para .csv
# somente para visualização rapida no excel

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[1][:-4] + ".csv"

# Lendo arquivo de input
with open(inputFile,'r') as input:
	lines = input.readlines()

# Removendo cabeçalho, caso exista
if lines[0][:5] == "Index":
	lines.pop(0)

# Escrevendo no arquivo de output
with open(outputFile,"w") as output:
	output.write("Index,Direction,Absolute Time,PID,Payload Length,Byte1,Byte2,Byte3,Byte4,Byte5,Byte6,Byte7,Byte8,\n")
	for line in lines:
		text = ""
		line = line.split()
		for _ in range(4):
			line.pop(4)
		for item in line:
			text += item + ","
		text = text[:-1] + "\n" 
		output.write(text)


