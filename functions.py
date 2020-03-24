# funcs.py
from classes import *


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

def getTimes(PID):
	return [i.time.sincestart for i in getAllPacketsWithPID(PID)]