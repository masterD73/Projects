# -------------------------
# title: TCP Client
# -------------------------
# -------------------------
# Description: Echo.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer:
# AI2 InfinityLabs.
# ----------------------------
# -------------------------
# title:
# -------------------------
# -------------------------
# Description:
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
import socket


def main():
    run_client()


def run_client():
    host = "127.0.0.1"
    port = 1786

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Message to send:")
            if message == "":
                s.sendall(b" ")
            if message == "close":
                s.sendall(message.encode())
                print("Connection closed.")
                break
            s.sendall(message.encode())
            data = s.recv(1024).decode()
            if data == "Connection terminated.":
                print(data)
                break
            print(f"message received: {data}")


if __name__ == "__main__":
    main()
