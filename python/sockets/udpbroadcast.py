# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
import socket
from time import sleep
UDP_IP = "<broadcast>"
UDP_PORT = 6060
connect_data = UDP_IP, UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))
sock.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(5)
while True:
    try:
        data, addr = sock.recvfrom(1024)

        sock.sendto(b"Daniel", addr)
        print(addr)
        print(f"received message:{data.decode()}")
        sleep(1)
    except TimeoutError:
        print("No data received. server terminated.")
        break
