from socket import *
myHost = ''
myPort = 50007

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((myHost, myPort))
sock.listen(5)

while True:
    connectin, address = sock.accept()
    print('Server connected by', address)
    while True:
        data = connectin.recv(1024)
        if not data: break
        connectin.send(b'Echo=>' + data)
    connectin.close()