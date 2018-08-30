import sys, os
import time, datetime
class tickData():
    def __init__(self):
        self.symbol=''
        self.price=0.0

        self.time=''
        self.size=0

def loaddata(symbol, length):







    market = symbol[-2:]

    os.chdir('D:\\data\\TOS\\' + market + '\\' + symbol)

    listd = os.listdir('D:\\data\\TOS\\' + market + '\\' + symbol)
    data = []
    for date in listd[-length:]:
        os.chdir(date)
        with open(symbol + '.txt') as fp:
            t = fp.readlines()

        os.chdir('D:\\data\\TOS\\' + market + '\\' + symbol)
        print len(data)
        data+=t
        for i in data:
            if i == '\n':
                data.remove(i)


        tickT = []
        for i in data:

            z=i.split(',')
            # print z[5]
            tick = tickData()
            tick.symbol = z[3][7:]
            tick.time = z[2][11:]
            tick.price = z[5][6:]
            tick.size = z[6][5:]
            tickT.append(tick)
            # print tick.price
        # time.sleep(1)

    return tickT
    #    for line in

if __name__ == "__main__":
    lists=['GLE.PA','SAN.PA','BNP.PA','CS.PA','LLOY.LO']
    for s in lists:
        print s
        T=loaddata(s,1)
        print len(T)
