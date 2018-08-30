import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s.connect(('127.0.0.1',4413))
# s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s1.listen((HOST, PORT))
s.connect(('127.0.0.1',33666))
i = 1

while True:
    data, addr = s.recvfrom(2048)

    print addr,data
    # s.sendto(data,('127.0.0.1',4415))
