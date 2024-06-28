import serial.tools.list_ports
import serial
from time import sleep
from datetime import datetime
import os

BAUDRATE = 115200
TIMEOUT = 1
ID_STRING = "arduino"
RETRY_COUNT = 20


def find_port():
    available_ports = list(serial.tools.list_ports.comports())

    for port in available_ports:
        p = serial.Serial(port.device, BAUDRATE, timeout=TIMEOUT)
        p.write("i".encode())
        retry = RETRY_COUNT
        while retry:
            if p.in_waiting:
                out = p.readline().decode().rstrip()
            else:
                sleep(0.01)
                retry -= 1
        p.close()
        if out == ID_STRING:
            return port.device


def get_enviro():
    port = find_port()
    p = serial.Serial(port, BAUDRATE, timeout=TIMEOUT)

    p.write("e".encode())

    retry = RETRY_COUNT
    while retry:
        if p.in_waiting:
            out = p.readline().decode().rstrip()
            return out
        else:
            sleep(0.05)
            retry -= 1
    return None


def get_sound(start_delay=0):
    port = find_port()
    p = serial.Serial(port, BAUDRATE, timeout=TIMEOUT)

    sleep(start_delay)
    p.write("s".encode())

    out = []
    retry = RETRY_COUNT
    while retry:
        if p.in_waiting:
            out.append(int(p.readline().decode().rstrip()))
            retry = RETRY_COUNT
        else:
            sleep(0.05)
            retry -= 1
    p.close()

    out_str = ""
    for element in out:
        out_str += str(element) + "\n"
    out_str = out_str[:-1]

    if len(out_str) > 0:
        return out_str
    else:
        return None


def get_imu(start_delay=0):
    port = find_port()
    p = serial.Serial(port, BAUDRATE, timeout=TIMEOUT)

    sleep(start_delay)
    p.write("a".encode())

    out = []
    retry = RETRY_COUNT
    while retry:
        if p.in_waiting:
            out.append(p.readline().decode().rstrip())
            retry = RETRY_COUNT
        else:
            sleep(0.05)
            retry -= 1
    p.close()

    out_str = ""
    for element in out:
        out_str += str(element) + "\n"
    out_str = out_str[:-1]

    if len(out_str) > 0:
        return out_str
    else:
        return None


def get_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    return timestamp


def save_data(folder, label, data):
    filename = get_timestamp() + ".csv"
    rel_directory = os.path.relpath(folder, os.getcwd())
    os.makedirs(os.path.dirname(rel_directory + "/"), exist_ok=True)
    with open(rel_directory + "/" + filename, "w") as data_file:
        data_file.write(data)
    with open(rel_directory + "/" + "labels.csv", "a") as label_file:
        label_file.write(filename + "," + label + "\n")
