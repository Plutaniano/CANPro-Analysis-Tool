import serial
import threading

ser = serial.Serial("COM6", 115200)

latest = ""
def serial_interface():
    while 1:
        global latest
        latest = ser.readline().decode("utf-8")[:-1]

t = threading.Thread(target=serial_interface)
t.start()