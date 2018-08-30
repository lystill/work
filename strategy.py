#coding=utf-8



jpGWbuy='JAPN%20Buy%20TSE%20Limit%20DAY'
jpGWsell='JAPN%20Sell->Short%20TSE%20Limit%20DAY'
deGwBuy='CHXE%20Buy%20CHIXXETRA%20Limit%20DAY'
deGwsell='CHXE%20Sell%20CHIXXETRA%20Limit%20DAY'
from bar import  bar
from loaddata import loaddata
from sendOrderThread import*
import talib as ta
import numpy as np

class strategy(object):

    def __init__(self,tradeEngine):



        self.onIntiLoadHist=True
        self.papiIndex = []
        self.tradeEngine=tradeEngine
        # self.eventEngine=eventEngine/WUSHURU
        self.i=0
        self.strategyName='strategy'
        self.kLen=3








       #  self.bar=barG(self.onbar)
       #  self.symbol=['BMW.DE','DAI.DE','zhishutick'] CHXE%20Buy%20CHIXXETRA%20Limit%20DAY
       #  self.symbol=['3188.HK','0939.HK','2327.HK','0175.HK']
       # self.symbol = ['BMW.DE','DAI.DE','SAP.DE','DTE.DE']
       #  self.symbol=['KROT3.BZ','CSNA3.BZ','PETR4.BZ','VALE3.BZ']
       #  self.symbol=['8411.JP','8306.JP','6502.JP','7201.JP','5301.JP','6501.JP','6752.JP','8604.JP']
        self.symbol=['BMW.DE','DAI.DE','BAS.DE','SAP.DE','BAYN.DE','TKA.DE','DTE.DE','LHA.DE','SIE.DE']
        self.symbolHistTickdata={}
        self.symbolBarDict = {}
        self.strategyOrderDict={}
        #state
        self.buySignalDict={}
        self.orderSendingDict={}
        self.buyTrigerPriceDict={}
        self.symbolpostionDict={}
        self.buyStopPriceDict={}
        self.buyTargetPriceDict={}


        for s in self.symbol:
            self.symbolBarDict[s]=bar(self.onBar,s,1)
            self.buySignalDict[s]=0
            self.orderSendingDict [s]= 0

            self.buyTrigerPriceDict [s]= 9999.99
            self.symbolpostionDict[s] = 0
            self.buyStopPriceDict[s] = 0.0
            self.buyTargetPriceDict[s] = 9999.99
        if self.onIntiLoadHist==True:
            self.onInit()
        # threads=[]
        # for t in threads:
        #     t.start()
        # t1=threading.Thread(target=tradeEngine.sendOrder,args=('8144.JP','300',jpGW,'100'))
        # t2 = threading.Thread(target=tradeEngine.sendOrder, args=('8144.JP', '300', jpGW, '100'))
        # # t1=threading.Thread(target=tradeEngine.sendOrder('VALE3.BZ','61','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100'))
        # # t2=threading.Thread(target=tradeEngine.sendOrder('VALE3.BZ','50','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100'))
        # t1.start()
        # t2.start()
        # t1.join()
        # t2.join()
        # tradeEngine.sendOrder('VALE3.BZ', '60', 'BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY', '100')
        # t2.start()


        # for i in range(2):
        #
        #
        #    # '/ExecuteOrder?limitprice=89.2&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE'
        #    #urlbz=sendhttp('/ExecuteOrder?limitprice=89.2&ordername=BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY&shares=100&symbol=VALE3.BZ')
        #
        #     # r=tradeEngine.sendOrder('BMW.DE','89.0','CHXE%20Buy%20CHIXXETRA%20Limit%20DAY','100')
        #     r=tradeEngine.sendOrder('VALE3.BZ','50','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100')



            # print r
            #
            # self.orderid.append(r)
            # print self.orderid

            # self.sendOrder('8411.JP', '193', jpGW, '100')

        # self.registerEvent(self,'tick')




    def onInit(self):

        for s in self.symbol:
            self.symbolBarDict[s].onInit = True

            intiData=loaddata(s,1)
            print len(intiData)
            print 'len of initData'
            self.symbolHistTickdata[s]=intiData

            for i in self.symbolHistTickdata[s]:
                # print i.price
                self.symbolBarDict[s].updateTick(i)
            # for i in self.symbolBarDict[s].barElist:
            #     print i.time, i.high,i.low, i.close, i.open,i.vol
            self.symbolBarDict[s].onInit=False
            print 'onInit False'




    def onTick(self,tick):
        print 'ontick'
        print self.symbol
        print tick.symbol,tick.size
        self.symbolBarDict[tick.symbol].updateTick(tick)
        #update Kline
        if self.orderSendingDict[tick.symbol]==0 and self.symbolpostionDict[tick.symbol]>0:
            if float(tick.price)>self.buyTargetPriceDict[tick.symbol]:
                self.orderSendingDict[tick.symbol] = 1
                print "buy closed"
                s2=sendOrderThread(tick.symbol,'sell',str(self.buyTargetPriceDict[tick.symbol]-0.10),deGwsell,self.symbolpostionDict[tick.symbol],self.strategyName,self.tradeEngine.eventEngine)
                s2.start()
            if float(tick.price)<self.buyStopPriceDict[tick.symbol]:
                self.orderSendingDict[tick.symbol]=1
                print"buy Stoped"
                s3=sendOrderThread(tick.symbol,'sell',str(self.buyStopPriceDict[tick.symbol]-0.10),deGwsell,self.symbolpostionDict[tick.symbol],self.strategyName,self.tradeEngine.eventEngine)
                s3.start()



        if self.buySignalDict[tick.symbol]==1 and self.orderSendingDict[tick.symbol]==0 and self.symbolpostionDict[tick.symbol]==0:
            #and self.orderSending[tick.symbol]==0:
            if tick.price>self.buyTrigerPriceDict[tick.symbol]:
                self.orderSendingDict[tick.symbol] = 1
                print "Buy Now!!!!"
                buyprice=str(float(tick.price)+0.10)
                # self.buyTargetPriceDict[tick.symbol]=(float(tick.price)-self.buyStopPriceDict[tick.symbol])*2+float(tick.price)
                log(buyprice+'buprice')
                # log(str( self.buyTargetPriceDict[tick.symbol])+"buyTarget")
                # s1=sendOrderThread(tick.symbol,'200','BVMF%20Buy%20BOVESPA%20Limit%20DAY',100,self.strategyName,self.tradeEngine.eventEngine)
                s1 = sendOrderThread(tick.symbol,'buy', buyprice, deGwBuy, 200, self.strategyName,self.tradeEngine.eventEngine)
                s1.start()




        # listClose=[]
        # print self.symbolBarDict[tick.symbol].barCount,'barcount'
        # print  self.symbolBarDict[tick.symbol].newBar,"barstart!@!@!@",self.symbolBarDict[tick.symbol].bar.time
        #
        # for i in self.symbolBarDict[tick.symbol].barElist[-self.kLen:]:
        #     print 'k=============='
        #     print i.time, i.high,i.low, i.close, i.open,i.vol
        #
        #
        #     listClose.append(i.close)
        # print listClose
        # print len(listClose)
    def onBar(self,bar1):
        print 'on bar in'
        print bar1.symbol
        print type(bar1)
        print bar1.barCount

        d=bar1.barElist[-self.kLen:]
        listClose = []
        listHigh=[]
        listLow=[]
        print 'listClose'
        for i in bar1.barElist[-self.kLen:]:
            print i.time, i.high, i.low, i.close, i.open, i.vol
            listClose.append(float(i.close))
            listHigh.append(float(i.high))
            listLow.append(float(i.low))
            print listClose
            print len(listClose)






        print bar1.symbol,bar1.barCount,'barcount','bar.symbol'
        if bar1.barCount>self.kLen:
            p=np.array(listClose)
            ma5=ta.MA(p,5)
            print ma5,"ma5"
            if ma5[-1]<ma5[-2]:

                self.buySignalDict[bar1.symbol]=1
                self.buyTrigerPriceDict[bar1.symbol]=float(listHigh[-2])
                self.buyStopPriceDict[bar1.symbol]=float(listLow[-1])
                self.buyTargetPriceDict[bar1.symbol]=float(listHigh[-2])+2.0*(float(listHigh[-2])-float(listLow[-1]))
                print "buy singal"
                log(str(self.buyStopPriceDict[bar1.symbol])+'buyStopPrice')
                log(str(self.buyTargetPriceDict[bar1.symbol]) + 'buyTargetPrice')







        if 0:
            self.buySignal=1
            self.trigerPrice=''
            self.StopPrice=''



    def onOrderEvent(self,orderEvent):
        print"onorder"
        print orderEvent.eventFlavour,'eventFlavour'
        orderNumber=orderEvent.orderNumber
        orderIdstrategyDict=self.tradeEngine.orderIdStrategyDict
        symbol=orderIdstrategyDict[orderNumber][1]
        side=orderIdstrategyDict[orderNumber][2]
        eventFlavour=orderEvent.eventFlavour
        price=orderEvent.price
        size=orderEvent.size
        description=orderEvent.description
        log('eventFlovur#@#!#@#!###')
        log(str(eventFlavour))
        log(str(type(eventFlavour)))
        if eventFlavour=='0':
            pass
        elif eventFlavour=='1':
            log('11111111111111111'+str(datetime.now())+'price:'+price+'size:'+size+'description:'+description)
        elif  eventFlavour=='2':
            print "newOrderAceepet"
            self.orderSendingDict[symbol]=0;

        elif eventFlavour=='3':
            if side=='buy':
                self.symbolpostionDict[symbol]=self.symbolpostionDict[symbol]+int(size)
            elif side=='sell':
                self.symbolpostionDict[symbol]=self.symbolpostionDict[symbol]-int(size)




        elif eventFlavour=='4':
            log('4444444444444444'+str(datetime.now())+'price:'+price+'size:'+size+'description:'+description)
            if side=='buy':
                self.symbolpostionDict[symbol]=self.symbolpostionDict[symbol]+int(size)
            elif side=='sell':
                self.symbolpostionDict[symbol]=self.symbolpostionDict[symbol]-int(size)
            print"all filled,ready!!zhisun"

        elif eventFlavour=='5':
            print "cancelled"
        elif eventFlavour=='6':
            print "rejected"

        elif eventFlavour=='7':
            pass
        elif eventFlavour=='8':
            print"NetWork Error"
        elif eventFlavour=='9':
            pass
        elif eventFlavour=='10':

            print "newOrder"
        elif eventFlavour=='11':
            pass
        else:
            log('?????????????????' + str(datetime.now()))









        # self.i=self.i+1
        # print 'sleep......................,',self.i

        # t1=threading.Thread(target=self.tradeEngine.sendOrder,args=('8144.JP','300',jpGW,'100'))
        # t1.start()
        # sendOrder1= sendOrderThread('8306.JP', '700', jpGW, '100', self.strategyName, self.tradeEngine.eventEngine)
        # 'BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY'
        # sendOrder1 = sendOrderThread('VALE3.BZ', '20', 'BVMF%20Buy%20BOVESPA%20Limit%20DAY', '100', self.strategyName, self.eventEngine)
        # sendOrder1=sendOrderThread('BMW.DE','90',deGw,'100',self.strategyName,self.tradeEngine.eventEngine)
        # sendOrder1.start()



        #tick >triger price buuy
        #he cheng Kxian


        # threads=[]
        # for t in threads:
        #     t.start()
        # t1=threading.Thread(target=tradeEngine.sendOrder,args=('8144.JP','300',jpGW,'100'))
        # t2 = threading.Thread(target=tradeEngine.sendOrder, args=('8144.JP', '300', jpGW, '100'))
        # # t1=threading.Thread(target=tradeEngine.sendOrder('VALE3.BZ','61','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100'))
        # # t2=threading.Thread(target=tradeEngine.sendOrder('VALE3.BZ','50','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100'))
        # t1.start()
        # t2.start()
        # t1.join()
        # t2.join()









        # threads=[]
        # for t in threads:
        #     t.start()
        # t1=threading.Thread(target=tradeEngine.sendOrder,args=('8144.JP','300',jpGW,'100'))
        # t2 = threading.Thread(target=tradeEngine.sendOrder, args=('8144.JP', '300', jpGW, '100'))
        # # t1=threading.Thread(target=tradeEngine.sendOrder('VALE3.BZ','61','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100'))
        # # t2=threading.Thread(target=tradeEngine.sendOrder('VALE3.BZ','50','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100'))
        # t1.start()
        # t2.start()
        # t1.join()
        # t2.join()
        # tradeEngine.sendOrder('VALE3.BZ', '60', 'BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY', '100')
        # t2.start()

        # for i in range(2):
        #
        #
        #    # '/ExecuteOrder?limitprice=89.2&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE'
        #    #urlbz=sendhttp('/ExecuteOrder?limitprice=89.2&ordername=BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY&shares=100&symbol=VALE3.BZ')
        #
        #     # r=tradeEngine.sendOrder('BMW.DE','89.0','CHXE%20Buy%20CHIXXETRA%20Limit%20DAY','100')
        #     r=tradeEngine.sendOrder('VALE3.BZ','50','BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY','100')

        # print r
        #
        # self.orderid.append(r)
        # print self.orderid

        # self.sendOrder('8411.JP', '193', jpGW, '100')

        # self.registerEvent(self,'tick')

















