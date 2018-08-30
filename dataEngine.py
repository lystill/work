import socket
from eventEngine import *
import sys,os
class tickData():
    def __init__(self):
        self.symbol=''
        self.price=0.0

        self.time=''
        self.size=0
class orderEvent():
    def __init__(self):
        self.localTime=''
        self.marketDateTime=''
        self.orderNumber=''
        self.originatorSeqId=100#1acceped  -18partFilled ++1
        self.eventFlavour=100# 3 wei wan  4 filled
        self.eventMessageType=100
        self.description=''

        self.eventOriginatorId=100
        self.price=0.0
        self.size=0# 3acpetd 2 opc pending
class pApiOrder(object):
    def __init__(self):
        self.localTime=''
        self.pApiIndex=0
        self.orderNumber=''
class strategyRequestId(object):
    def __init__(self):
        self.strategyName=''
        self.requestId=''
        self.symbol=''
        self.side=''
class dataEngine(object):
    def __init__(self,eventEngine):
        self.dateToday= None
        self.HOST = ''
        self.PORT = 33666
        self.eventEngine=eventEngine
        self.listen(self.HOST,self.PORT)

    def listen(self,HOST, PORT):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


        s.bind((HOST, PORT))



        i = 1

        while True:
            data, addr = s.recvfrom(2048)
            # print addr

            if not data:
                print "client has exist"
                break

            d = data.split(',')
            message = d[1][8:]
            if message == 'TOS':
                symbol = d[3][7:]
                market = symbol[-2:]
                date = d[-1][5:15]
                price = d[5][6:]
                size=d[6][5:]

                type=d[4][5:]
                if type=='0':

                    # print data
                    if self.dateToday==None and d[-1][5:15]!='\n':
                        self.dateToday=d[-1][5:15]
                    if self.dateToday!=None:

                        d1 = data.split(',')
                        # tickdata = {}
                        # tickdata['symbol'] = d1[3][7:]
                        # tickdata['markettime'] = d1[2][11:]
                        #
                        # tickdata['price'] = d1[5][6:]
                        # event = Event();
                        # event.type_ = 'tick'
                        # event.dict_ = tickdata
                        tick=tickData()
                        tick.time=d1[2][11:]
                        tick.symbol=d1[3][7:]
                        tick.price=d1[5][6:]
                        tick.size=d1[6][5:]
                        event = Event();
                        event.type_ = 'EVENT_tick'
                        event.dict_ = tick
                        event.puttime=datetime.datetime.now()


                        self.eventEngine.put(event)

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
            if message=="OrderEvent":
                # print message,'dataEnginge'
                # print data
                # d1 = data.split(',')
                orderData=orderEvent()
                orderData.eventFlavour=d[6][13:]
                orderData.orderNumber=d[3][12:]
                orderData.price=d[8][6:]
                orderData.size=d[9][5:]
                orderData.eventMessageType=d[5][17:]
                orderData.description=d[10][13:]+d[11]
                # print orderData.eventFlavour, orderData.orderNumber, orderData.price, orderData.size, orderData.eventMessageType, orderData.description
                # orderData.price=
                # orderData.size=
                event = Event()
                event.type_ = 'EVENT_orderEvent'
                event.dict_ = orderData
                event.puttime = datetime.datetime.now()
                self.eventEngine.put(event)
                # print orderData.eventFlavour,orderData.orderNumber,orderData.price,orderData.size,orderData.eventMessageType,orderData.description


            elif message=="OrderStatus":
                pass
                # print message
                # print data
            elif message=="PAPIORDER":
                papiorder=pApiOrder()
                papiorder.localTime=d[0][10:]
                papiorder.orderNumber=d[3][12:-1]
                papiorder.pApiIndex=d[2][13:]
                # print papiorder.orderNumber,papiorder.pApiIndex
                event=Event()
                event.type_='EVENT_PAPIORDER'
                event.dict_=papiorder
                event.puttime = datetime.datetime.now()
                self.eventEngine.put(event)


                # print message,'dataEngine'
                # print papiorder.pApiIndex,papiorder.orderNumber
            else:
                pass

            #  z=os.getcwd()
            # datarecoder(data)

            # print "received:", data, "from", addr

        s.close()
if __name__=="__main__":
    ee=eventEngine()
    d1=dataEngine(ee)