import socket

def listen(HOST,PORT):



    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST,PORT))
    i=1
    while True:
        data, addr = s.recvfrom(2048)
        if not data:
            print "client has exist"
            break


        print data.split(',')
        i=i+1
        print i

       # print "received:", data, "from", addr

    s.close()