# funcs.py
from classes import *
from matplotlib import pyplot as plt


# Retorna todos os Packets que tenham o PID especificado
def getAllPacketsWithPID(PID):
	lista = []
	if type(PID) is str:
		PID = PIDs[PID]
	for i in Packets:
		if i.PID.hex == PID.hex:
			lista.append(i)
	return lista

# Seleciona todos os pacotes com o PID especificado e retorna
# os bytes do intervalo especificado de todos os pacotes
def getBytes(PID,start = 0,end = 0):
	lista = getAllPacketsWithPID(PID)
	bytes = []
	for i in lista:
		if start == 0 and end == 0:
			bytes.append(float(int("".join(i.payload.bytes),16)))
		if start != 0:
			bytes.append(float(int(i.payload.bytes[start],16)))
	return bytes

# Retorna todos os time.sincestart do PID especificado
def getTimes(PID):
	return [i.time.sincestart for i in getAllPacketsWithPID(PID)]

# print() todos os pacotes com o PID especificado
def printPackets(PID):
	lista = getAllPacketsWithPID(PID)
	for i in lista:
		print(i)

# Produz um gráfico dos payloads de pacotes com PID especificado
# se não for especificado um começo e um fim,
def plotPID(PID,start = 0, end = 0):
	plt.plot(getTimes(PID),getBytes(PID, start, end))
	printPackets(PID)
	plt.show()

def getPIDstats():
	stats = {}
	for i in list(PIDs.keys()):
		stats[i] = 0
	for i in Packets:
		stats[str(i.PID)[6:]] += 1
	for key, value in sorted(stats.items(), key=lambda item: item[1]):print("%s: %s" % (key, value))

