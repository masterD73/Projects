# -------------------------
# title: UDP Server
# -------------------------
# -------------------------
# Description: Echo.
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 65432
connect_data = UDP_IP, UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(connect_data)
sock.settimeout(5)
while True:
    try:
        data, addr = sock.recvfrom(1024)

        sock.sendto(b"hi from server", addr)
        print(f"received message:{data.decode()}")
    except TimeoutError:
        print("No data received. server terminated.")
        break


