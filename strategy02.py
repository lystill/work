##coding=utf-8


#coding=utf-8

jpGW='JAPN%20Buy%20TSE%20Limit%20DAY'
deGw='CHXE%20Buy%20CHIXXETRA%20Limit%20DAY'
from bar import  bar
from loaddata import loaddata
from sendOrderThread import*




class strategy02(object):

    def __init__(self,tradeEngine):




        self.papiIndex = []
        self.tradeEngine=tradeEngine
        # self.eventEngine=eventEngine/WUSHURU
        self.i=0
        self.strategyName='strategy02'






       #  self.bar=barG(self.onbar)
       #  self.symbol=['BMW.DE','DAI.DE','zhishutick'] CHXE%20Buy%20CHIXXETRA%20Limit%20DAY
       #  self.symbol=['3188.HK','0939.HK','2327.HK','0175.HK']
        self.symbol = []#['BMW.DE','DAI.DE','GLE.PA','BNP.PA','CS.PA']
        # self.symbol=['8411.JP','8306.JP','6502.JP','7201.JP','1088.HK','0939.HK','0175.HK','3328.HK']
        self.symbolHistTickdata={}
        self.symbolBarDict = {}
        self.strategyOrderDict={}
        for s in self.symbol:
            self.symbolBarDict[s]=bar(1)



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

            intiData=loaddata(s,1)
            print len(intiData)
            print 'len of initData'
            self.symbolHistTickdata[s]=intiData

            for i in self.symbolHistTickdata[s]:
                # print i.price
                self.symbolBarDict[s].updateTick(i)
            # for i in self.symbolBarDict[s].barElist:
            #     print i.time, i.high,i.low, i.close, i.open,i.vol



    def onTick(self,tick):
        print 'ontick'
        print self.symbol
        print tick.symbol,tick.size
        self.symbolBarDict[tick.symbol].updateTick(tick)
        # time.sleep(1)
        # self.i=self.i+1
        # print 'sleep......................,',self.i

        # t1=threading.Thread(target=self.tradeEngine.sendOrder,args=('8144.JP','300',jpGW,'100'))
        # t1.start()

        # sendOrder2 = sendOrderThread('8411.JP', '92', jpGW, '100', self.strategyName, self.tradeEngine.eventEngine)
        # #'BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY'
        # # sendOrder1 = sendOrderThread('VALE3.BZ', '20', 'BVMF%20Buy%20BOVESPA%20Limit%20DAY', '100', self.strategyName, self.eventEngine)
        # sendOrder1 = sendOrderThread('8411.JP', '92',jpGW, '100', self.strategyName, self.eventEngine)
        # sendOrder2=sendOrderThread('DAI.DE','60',deGw,'100',self.strategyName,self.tradeEngine.eventEngine)
        # sendOrder2.start()

        # sendOrder1.join()
        # id=sendOrder1.get_sendOrderIndex()
        # print id,"!@@@!!@!@!@!@!@!@!@!@!@!@!@!@!@"
        # print sendOrder1.get_sendOrderIndex(),"!@@@!!@!@!@!@!@!@!@!@!@!@!@!@!@"

        # print self.symbolBarDict[tick.symbol].barE
        for i in self.symbolBarDict[tick.symbol].barElist:
            print i.time, i.high,i.low, i.close, i.open,i.vol
        # r = self.tradeEngine.sendOrder('BMW.DE', '89.0', 'CHXE%20Buy%20CHIXXETRA%20Limit%20DAY', '100')
        #sending order

        # r = self.tradeEngine.sendOrder('LLOY.LO', '62', 'LSE%20Buy%20LSE%20Limit%20DAY', '100')
        #
        # self.papiIndex.append(r)
        # print '##########################,strategy'
        # print datetime.datetime.now()
        # print r

        # self.bar.updateTick(tick)
        # print self.bar.bar
        # print

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