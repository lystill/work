import socket
import time
HOST='127.0.0.1'
PORT=4134
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


s.connect((HOST,PORT))
i=1
while True:
    i=i+1
    print i

    data = s.recv(1024)
    print data

