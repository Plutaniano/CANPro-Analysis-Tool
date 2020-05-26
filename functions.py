# functions.py
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
def get_bytes(payload, interval=None):
	new_lista = []
	limits = []
	if interval == None:
		interval = f"1-{payload.size}"
	lista = interval.split(",")
	for i in range(len(lista)):
		lista[i] = lista[i].strip().replace(" ","")
	for i in lista:
		if len(i) == 1:
			new_lista.append(int(i))
		if len(i) > 1:
			limits = [int(i.split("-")[0]),int(i.split("-")[1])+1]
			for j in range(limits[0],limits[1]):
				new_lista.append(j)
	lista = []
	for i in new_lista:
		lista.append(payload.bytes[i-1])
	return lista

# Retorna todos os time.sincestart do PID especificado
def getTimes(PID):
	return [i.time.sincestart for i in getAllPacketsWithPID(PID)]


# print() todos os pacotes com o PID especificado
def printPackets(PID):
	last = 0
	lista = getAllPacketsWithPID(PID)
	for i in lista:
		if i.payload.bytes != last:
			print(i)


# Produz um gráfico dos payloads de pacotes com PID especificado
# se não for especificado um começo e um fim,
def plotPID(PID, interval=None):
	plt.plot(getTimes(PID),get_bytes_all_PIDs(PID, interval))
	printPackets(PID)
	plt.show()

def get_bytes_all_PIDs(PID, interval):
	lista = []
	for i in getAllPacketsWithPID(PID):
		lista.append(get_bytes(i.payload,interval))
	for i in range(len(lista)):
		lista[i] = int("".join(lista[i]),16)
	return lista

# print() todos os pacotes processados
def print_Packets():
	for i in Packets:
		print(i)

def PID_stats():
	stats = {}
	for i in list(PIDs.keys()):
		stats[i] = 0
	for i in Packets:
		stats[str(i.PID)[6:]] += 1
	for key, value in sorted(stats.items(), key=lambda item: item[1]):print(f'{key}: {float(value):5.0f}')

