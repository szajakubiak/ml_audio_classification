import serial
from time import sleep

port = "COM10"
baudrate = 115200

p = serial.Serial(port, baudrate, timeout=1)

def get_enviro():
    p.write("e".encode())

    retry = 20
    while retry:
        if p.in_waiting:
            out = p.readline().decode().rstrip()
            return out
        else:
            sleep(0.05)
            retry-=1
    return None

def get_sound():
    p.write("s".encode())
    
    out = []
    retry = 40
    while retry:
        if p.in_waiting:
            out.append(int(p.readline().decode().rstrip()))
        else:
            sleep(0.05)
            retry-=1
    if len(out) > 0:
        return out
    else:
        return None

