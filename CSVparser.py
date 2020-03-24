# CSVparser.py

# transforma arquivo .csv em uma lista contendo as listas de cada linha
def CSVparser(filename):
	with open(filename,"r") as file:
		lines = file.readlines()
		lines.pop(0)
		for i in range(len(lines)):
			lines[i] = lines[i]
		# removendo \n do ultimo byte
		for i in range(len(lines)):
			lines[i] = lines[i][:-1]
	file.close()
	return lines



