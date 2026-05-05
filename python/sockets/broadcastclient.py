# -------------------------
# title: UDP Broadcast
# -------------------------
# -------------------------
# Description: Client side.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
import socket
PORT = 6060
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", PORT))
while True:
    data = s.recv(1024)
    print(f"Received {data.decode()}")
