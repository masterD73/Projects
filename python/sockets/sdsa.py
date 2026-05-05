# -------------------------
# title: TCP Server Mult
# -------------------------
# -------------------------
# Description: Echo.
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer:
# AI2 InfinityLabs.
# ------------------------------
import sys
import socket

import select
from threading import Thread


def main():
    run_server()


def handle_client(conn, addr):
    while True:
        try:
            data = conn.recv(1024).decode()
        except Exception as e:
            print(f"Error: {e}")
            break
        else:
            if data == "close":
                print(f"Connection of client {addr} ended.")
                break
            print(f"Message received: {data}")
            response = input(f"Server message to send to {addr}:")
            if response == "":
                conn.send(b" ", addr)
            if response.lower() == "close":
                conn.send(b"Connection terminated.")
                print(f"Connection of client {addr} ended.")
                break
            try:
                conn.send(response.encode())
            except Exception as e:
                print(f"Error: {e}")


def run_server():
    server_ip = "127.0.0.1"
    port = 1786
    possible_connections = 9000

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((server_ip, port))
        s.listen(possible_connections)
        print(f"Listening on {server_ip}:{port}")
        inputs = [s]
        while True:
            readable, writeable, exceptional = select.select(inputs, [], [])
            for sock in readable:
                if sock == s:
                    conn, addr = s.accept()
                    inputs.append(conn)
                    print(f"Connected by {addr}")
                    thread = Thread(target=handle_client, args=(conn, addr))
                    thread.start()
                elif sock == sys.stdin:
                    sys.stdin.readline()
                    break
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
