from register_stock import *
# from socket_listen import *
from Queue import Queue, Empty
from threading import Thread
from eventEngine import *
from strategy import *
import os, sys
import time, datetime

# ee = eventEngine()

i = 1
# while True:
#     ee.put('s'*i)
#     time.sleep(1)
#     i=i+1


import socket

HOST = '127.0.0.1'
PORT = 4413

# register(url_L1_Setuotput,stock)
# def datarecoder(data):
#     symbol=data[3]
#     fd=os.open('tick.csv')
#     os.write(fd,data)



class dataRecorder(object):
    def __init__(self,eventEngine):
        self.dateToday= None
        self.HOST = '127.0.0.1'
        self.PORT = 4413
        # self.eventEngine=eventEngine
        self.listen(self.HOST,self.PORT)

    def listen(self,HOST, PORT):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((HOST, PORT))
        # s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s1.bind((HOST, PORT))
        i = 1

        while True:
            data, addr = s.recvfrom(2048)

            if not data:
                print "client has exist"
                break

            d = data.split(',')

            message = d[1][8:]
            symbol = d[3][7:]
            market = symbol[-2:]
            date = d[-1][5:15]
            price = d[5][6:]
            size=d[6][5:]

            # print date
            # print price,type(price)

            # print message ,symbol ,market,datetime.datetime.now()
            # print '================================================================================'
            # LocalTime=22:49:17.678,Message=TOS,MarketTime=00:00:00.000,Symbol=GLE.PA,Type=1,Price=0,Size=0,Source=0,Condition=,Tick= ,Mmid= ,SubMarketId=0,Date=

            if message == 'TOS':
                print data
                if self.dateToday==None and date!='\n':
                    self.dateToday=date
                if self.dateToday!=None:

                    os.chdir('d:\\data\\TOS')
                    if not os.path.exists(market):
                        os.makedirs(market)
                        print '%s is not exits' % market
                    os.chdir(market)
                    if not os.path.exists(symbol):
                        os.makedirs(symbol)
                        print '%s is not exits' % symbol
                    os.chdir(symbol)
                    if not os.path.exists(self.dateToday):
                        print data
                        os.makedirs(self.dateToday)
                        print '%s is not exits' % date
                    os.chdir(self.dateToday)

                    fo = open(str(symbol) + '.txt', 'a+')
                    fo.write(str(data) + '\n')
                    fo.close()
                    i = i + 1
                    # print i

                    d1 = data.split(',')
                    tickdata = {}
                    tickdata['symbol'] = d1[3][7:]
                    tickdata['markettime'] = d1[2][11:]

                    tickdata['price'] = d1[5][6:]
                    # event = Event();
                    # event.type_ = 'tick'
                    # event.dict_ = tickdata
                    #
                    # self.eventEngine.put(event)

                    # os.makedirs(t)

                    # with open('/path/to/file', 'r') as f:
                    #    print f.read()
                    #    try:
                    #    f = open('/path/to/file', 'r')
                    #    print f.read()
                    # finally:
                    #    if f:
                    #        f.close()

                # print d[12],d[3],d[5],d[6]
                # d12 symbol

            #  z=os.getcwd()
            # datarecoder(data)

            # print "received:", data, "from", addr

        s.close()

if __name__=="__main__":

    d1=dataRecorder(ee)

