import socket

#Bir soket oluşturuyoruz
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Oluşturduğumuz soketi hostname 1234 numarası ile bind ediyoruz
s.bind((socket.gethostname(),1234))
s.listen(5)


while True:
    clientsocket,address  = s.accept()
    print(f"Conneciton from {address} has been established !")
    clientsocket.send(bytes("Welcome to the server!","utf-8"))


