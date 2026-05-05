# -------------------------
# title: UDP Client
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
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
MESSAGE = b"Hello world. Get me out of here. Please."
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    for i in range(5):
        s.sendto(MESSAGE, (HOST, PORT))
        data = s.recv(1024)
        print(f"Received {data.decode()}")
            
