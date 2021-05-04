
import socket
import tqdm
import os
import time
import socket
from pathlib import Path
import math

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

host = "192.168.254.132"

port = 5005

filename = "test2.txt"



def transfer(host, filename, port):
    filesize = os.path.getsize(filename)
    p = Path(filename)
    timestamp = math.floor(p.stat().st_mtime)
    # Making the client socket
    s = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    privateIP = socket.gethostbyname(socket.gethostname())

    s.send(f"{privateIP}{SEPARATOR}{timestamp}{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

    s.close()








def run(clients, filename):
    while True:
        for i in clients:
            try:
                transfer(i, filename, 5005)
            except:
                print("errors")

