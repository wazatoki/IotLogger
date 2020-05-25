import threading
import time

import serial



def parse_data(recv_data):
    print("parse data")

def watch():

    comport = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,timeout=1)
    recv_data = comport.read(400)
    comport.close()
    t=threading.Timer(2, watch)
    t.start()

def start_watch():
    t=threading.Thread(target=watch)
    t.start()