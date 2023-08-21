import socket
import threading
from typing import FrozenSet


HEADER = 64
PORT = 5050                      # Herhangi bir port atadık (8080 dışında)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


# Servera ulaşma şekilleri 

# SERVER = "192.168.25.116"

# Bu kod dizini otomotik olarak IPv4 address değerini gösterir = 192.168.25.116
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                   #  Server oluşturduk
server.bind(ADDR)                                                          # Server Üzerinden portu bağlıyoruz 




def HandleClient(conn,addr):
    print("[NEW CONNECTION] {} connected.".format(addr))
    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()
        

def Start():
    server.listen()
    print("[LISTENING] Server is listening on {}".format(SERVER))
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=HandleClient,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count()-1}")


print("[STARTING] server is starting !")
Start()

