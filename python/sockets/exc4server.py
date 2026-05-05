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
import socket
import select


class Reactor:

    def __init__(self, host="", port=5050):
        self.inputs = []
        self.outputs = []
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run_server(self):
        conn, addr = self.server_socket.accept()
        self.inputs.append(conn)


        while self.inputs or self.outputs:
            readables, writables, exceptionals = select.select(self.inputs, self.outputs, self.inputs, 1)
            for writable in writables:
                print("writable")
                response = input(f"Server message to send:")
                if response == "":
                    writable.send(b" ")
                elif response.lower() == "close":
                    writable.send(b"Connection terminated.")
                    print(f"Connection of client {writable} ended.")
                    writable.close()
                    self.outputs.remove(writable)
                    break
                else:
                    writable.send(response.encode())
                    if writable in self.outputs:
                        self.outputs.remove(writable)



            for error in exceptionals:
                print(f"Error received: {error}")
                error.close()
                self.inputs.remove(error)

    def subscribe_socket(self, sock, mode, func):
        if mode == "r":
            self.inputs.append(sock)
        elif mode == "w":
            self.outputs.append(sock)

    def unsubscribe_socket(self, sock, mode):
        sock.close()
        try:
            self.inputs.remove(sock)
        except Exception as e:
            print(e)

    def sockets(self):
        return self.inputs

    def reader(self):
        for readable in self.readables:
            if readable is self.server_socket:
                print("readable")
                conn, addr = readable.accept()
                self.inputs.append(conn)
            else:
                data = conn.recv(1024).decode()
                print(data)
            if data == "close":
                print(f"Connection of client {addr} ended.")
                conn.close()
                break
            print(f"Message received from {addr}: {data}")
            readable.close()
            self.inputs.remove(readable)
            break
def main():
    host, port = "", 11111
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(False)
    s.bind((host, port))
    s.listen()
    print("Sock is listening.")
    react = Reactor(host, port)
    react.subscribe_socket(s, "r")
    print("run")
    react.run_server()


if __name__ == "__main__":
    main()
