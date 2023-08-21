import socket


HEADER = 64
PORT = 5050                      
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.25.116"                                   # SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)      # client.connect(socket.gethostname(),5050)   bu işlemi gerçekleşirmiş olduk

def Send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght += b" " * (HEADER-len(send_lenght))
    client.send(send_lenght)
    client.send(message)


Send("Hello World")
input("Enter")
Send("Hello Everyone")
input("Enter")
Send("Hello Özgür")

Send(DISCONNECT_MESSAGE)
