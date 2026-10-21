# SPS
# Copyright (c) 2026 real-addkab
# Licensed under the GNU GENERAL PUBLIC LICENSE VERSION 3

import socket

host = input("enter an ip or website:\n")
ip = socket.gethostbyname(host)

def scan():
    for port in range(50,1000):
        try:
            sacket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sacket.settimeout(0.2)
            result = sacket.connect_ex((ip,port))
            if result == 0:
                print(f"Port {port} Open")
            sacket.close()
        except OSError:
            sacket.close()


if __name__ == "__main__":
    scan()