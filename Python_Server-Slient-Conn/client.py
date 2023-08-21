import socket

#Bir soket oluşturuyoruz
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# luşturduğumuz sokete bind ettiğimiz hostname ile bağlanıyoruz
s.connect((socket.gethostname(),1234))


while True:
    #tek seferde kaç byte ekrana yazacak
    msg = s.recv(8)

    # oluşturulan mesajı utf-8 charseti ile ekrana yazdırıyoruz.
    print(msg.decode("utf-8"))
