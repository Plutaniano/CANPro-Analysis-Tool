# GUI.py

from tkinter import *
from tkinter import scrolledtext

def refresh():
    txtbox.delete('1.0',END)

def loadfile():
    # load file
    pass

window = Tk()

window.title("CANPro Analysis Tool")
window.geometry('600x400')

PID_lb = Label(window, text='PID', font=('Arial Bold',15))
PID_lb.grid(column=0, row=0)
PID_entry = Entry(window, width=10, textvariable=StringVar(window, value='0x000'))
PID_entry.grid(column=1,row=0)

Refresh_btn = Button(window, text="Refresh", command=refresh)
Refresh_btn.grid(column=3,row=0)

bytes_entry = Entry(window, width=10)
bytes_entry.grid(column=1,row=1)
bytes_lb = Label(window, text='Bytes')
bytes_lb.grid(column=0,row=1)

Loadcsv_btn = Button(window, text="Load .csv", command=loadfile)
Loadcsv_btn.grid(column=3,row=1)

txtbox = scrolledtext.ScrolledText(window, width=70, height=20)
txtbox.grid(column=0,row=4,columnspan=20)

window.mainloop()