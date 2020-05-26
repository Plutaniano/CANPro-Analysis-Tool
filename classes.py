# classes.py

# Listas/dicionario de classes
Packets = []
PIDs = {}


# Classe Packet
class Packet:
    def __init__(self, line):
        line = line.split(",")
        self.index = len(Packets)
        self.direction = line[1]
        self.time = Time(line[2])
        self.PID = PIDUniquenessChecker(line[3])
        self.payload = Payload(line[5:])
        Packets.append(self)

    def __repr__(self):
        return f'({self.time.sincestart:07.3f})[{self.index:05.0f}]  {self.PID.hex}  [{self.payload.size}]   {" ".join(self.payload.bytes)} | {" ".join(self.payload.bytes_bin)}'


# Classe Time
# Variáveis para cálculo de tempo relativo
start = 0
last = 0


class Time:
    def __init__(self, time):
        global start, last
        self.clocktime = time
        if start == 0:
            start = timeFix(time)
            self.sincestart = 0
        else:
            self.sincestart = round(timeFix(time) - start, 4)
        self.sincelast = round(timeFix(time) - last, 4)
        lasttime = timeFix(time)

# Classe PID


class PID:
    def __init__(self, pid):
        self.hex = "0x" + pid[-3:]
        self.dec = int(self.hex, 16)
        self.description = ""  # Descrição do PID TODO
        PIDs[self.hex] = self

    def __repr__(self):
        return "[PID] " + self.hex

# Classe Payload


class Payload:
    def __init__(self, bytes):
        self.bytes = bytes
        self.bytes_bin = [bin(int(i, 16))[2:].zfill(8) for i in self.bytes]
        self.size = len(bytes)

    def __repr__(self):
        return " ".join(self.bytes)


# Função para transformar o tempo absoluto fornecido pelo
# CANPro em tempo relativo, em segundos
def timeFix(string):
    hours = int(string[:2]) * 60 * 60 				# horas em segundos
    minutes = int(string[3:5]) * 60 				# minutos em segundos
    seconds = int(string[6:8])	  				# segundos
    fraction_second = float(string[9:]) * 0.001 	# frações de segundo
    total = hours + minutes + seconds + fraction_second
    return total

# Checka se já existe um objeto para aquele PID
# se existir, retorna ele, se não, cria o objeto


def PIDUniquenessChecker(pid):
    if pid in PIDs:
        return PIDs[pid[-3:]]
    else:
        return PID(pid)
