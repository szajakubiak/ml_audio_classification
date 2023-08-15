import serial.tools.list_ports
import serial
from time import sleep

baudrate = 115200

p = serial.Serial(port, baudrate, timeout=1)

def find_port():
    available_ports = list(serial.tools.list_ports.comports())

    for port in available_ports:
        p = serial.Serial(port.device, baudrate, timeout=1)
        p.write("i".encode())
        retry = 20
        while retry:
            if p.in_waiting:
                out = p.readline().decode().rstrip()
            else:
                sleep(0.01)
                retry-=1
        p.close()
        if out == "arduino":
            return port.device

def get_enviro():
    port = find_port()
    p = serial.Serial(port, baudrate, timeout=1)

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

def get_sound(start_delay = 0):
    port = find_port()
    p = serial.Serial(port, baudrate, timeout=1)

    sleep(start_delay)
    p.write("s".encode())
    
    out = []
    retry = 40
    while retry:
        if p.in_waiting:
            out.append(int(p.readline().decode().rstrip()))
        else:
            sleep(0.05)
            retry-=1
    p.close()
    if len(out) > 0:
        return out
    else:
        return None

