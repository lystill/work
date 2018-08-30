# encoding: UTF-8
'''
策略引擎
'''

import numpy as np
import datetime
from collections import OrderedDict
from eventEngine import *
from sendhttp import *
from threading import  Thread
import xml.etree.ElementTree as ET
import traceback
from p8Function import *
import json
from strategy import strategy
from strategy02 import  strategy02
from  loaddata import *
# from multiprocessing import Pool
from dataEngine import *


class tradeEngine(object):
    settingFileName = 'trading_setting.json'

    settingfilePath = getJsonPath(settingFileName, __file__)
    def __init__(self,eventEngine):
        self.eventEngine = eventEngine
        # self.today=datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self.symbolRequest=[]
        self.strategyDict={}
        self.strategyTickDict={}
        self.strategyOrderDict={}
        self.tickProcessDict={}
        self.apiIndexOrderDict={}
        self.indexStrategyDict={}
        self.orderIdStrategyDict={}
        self.strategyNameDict={}
  # self.symboldict={}
        self.registerEvent()
        self.po={}
        self.id=None
        self.loadStrategy()

    # def sendOrder(self, symbol, price,gateway, size):
    #     #'/ExecuteOrder?limitprice=89.2&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE'
    #     sendurl = '/ExecuteOrder?symbol=%s&limitprice=%s&ordername=%s&shares=%s'%(symbol, price, gateway, size)
    #
    #     print sendurl
    #     z=sendhttp(sendurl)
    #     root = ET.fromstring(z)
    #     self.id = root[0].text
    #
    #     url_getordernumber='/GetOrderNumber?requestid=%s'%self.id
    #     # 这里ordernumber可能获取不到 由于网络原因
    #     z1=sendhttp(url_getordernumber)
    #     if z1=='Error':
    #         return 'Error'
    #     root=ET.fromstring(z1)
    #     ordernumber=root[0].text
    #     print ordernumber
    #     return ordernumber
    #     # sendhttp(http://localhost:8080/ExecuteOrder?symbol=2768.JP&limitprice=300&ordername=JAPN Buy TSE Limit DAY&shares=100)
       # sendhttp()CHXE%20Buy%20CHIXXETRA%20Limit%20DAY
    # def sendOrder(self, symbol, price,gateway, size):
    #     #'/ExecuteOrder?limitprice=89.2&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE'
    #     sendurl = '/ExecuteOrder?symbol=%s&limitprice=%s&ordername=%s&shares=%s'%(symbol, price, gateway, size)
    #
    #     print sendurl
    #     r=sendhttp(sendurl)
    #     root = ET.fromstring(r)
    #
    #     id = root[0].text
    #     return id

    def cancelOrder(self,orderId):
        pass
    def sendStopOrder(self,symbol,ordername,price,size,strategy):

        pass

    def putZhishuTickEvent(self, event):

        print event.dict_['symbol']
        self.po[event.dict_['symbol']] = event.dict_['price']
        # print self.po
        print len(self.po)
        # hecheng
        if len(self.po) > 2:
            z = 0.0
            valueList = []
            for s in self.po.iterkeys():
                t = float(self.po[s])
                valueList.append(t)
                z = z + t

            print valueList, z
            fo = open('d:\\zhishu.txt', 'a+')
            fo.write(str(z) + '\n')
            fo.close()

            event = Event();
            event.type_ = 'zhishutick'
            event.dict_ = {'zhishu': z}
            self.eventEngine.put(event)
    def registerEvent(self):
        #EVENT_requestId
        # self.eventEngine.register(EVENT_TICK, self.processTickEvent)
        self.eventEngine.register('EVENT_tick', self.processTickEvent)
        self.eventEngine.register('EVENT_requestId',self.processRequestId)
        print 'Event_reuestId register'
        self.eventEngine.register( 'EVENT_orderEvent',self.processOrderEvent)
        self.eventEngine.register('EVENT_PAPIORDER',self.processApiIndexEvent)
        # self.eventEngine.register(EVENT_TRADE, self.processTradeEvent)
        # self.eventEngine.register(EVENT_POSITION, self.processPosEvent)





    def processTickEvent(self,event):
        # putZhishuTickEvent
        symbol = event.dict_.symbol
        # print "tick time++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        # print 'puttime',event.puttime
        # print 'gettime',datetime.datetime.now()
        # log("tick time++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # log('puttime'+str(event.puttime))
        # log('gettime'+str(datetime.datetime.now()))

        # print 'event symbol',symbol,self.symbolRequest
        if event.dict_.symbol in self.symbolRequest:
            print self.tickProcessDict[symbol]
            print 'in reques',datetime.datetime.now()

            for l in self.tickProcessDict[symbol]:
                l.onTick(event.dict_)


    def processzhishuTickEvent(self,event):

        print "zhishu",event.dict_
    def processApiIndexEvent(self,event):

        # papiorder = pApiOrder()
        # papiorder.localTime = data[0][10:]
        # papiorder.orderNumber = data[3][12:]
        # papiorder.pApiIndex = data[2][13:]
        # event = Event()
        # event.type_ = 'PAPIORDER'
        # event.dict_ = papiorder
        # self.eventEngine.put(event)
        print "processapiIdexEvent!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print 'puttime',event.puttime
        print 'gettime',datetime.datetime.now()
        log("processapiIdexEvent++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        log('puttime'+str(event.puttime))
        log('gettime'+str(datetime.datetime.now()))
        print event.dict_.pApiIndex,event.dict_.orderNumber,
        self.apiIndexOrderDict[event.dict_.pApiIndex]=event.dict_.orderNumber
        for k,v in self.apiIndexOrderDict.items():
            print k,v
            log(str(k) + str(v) + "apiIndexOrderDict!!!!!!")

        strategyName=self.indexStrategyDict[event.dict_.pApiIndex]
        self.orderIdStrategyDict[event.dict_.orderNumber]=strategyName
        print "orderIdStrategyDict!!!!!!"


        for k,v in self.orderIdStrategyDict.items():
            print k,v
            log('k:++++'+str(k)+'v:+++++++'+str(v)+"orderIdStrategyDict!!!!!!")


    def processStopOrder(self,tick):


        pass
    def processOrderEvent(self,event):
        print "processOrederEvent++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print 'puttime',event.puttime
        print 'gettime',datetime.datetime.now()
        log("processOrederEvent++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        log('puttime'+str(event.puttime))
        log('gettime'+str(datetime.datetime.now()))

        orderNumber=event.dict_.orderNumber
        eventFlavour=event.dict_.eventFlavour
        strategyname=self.orderIdStrategyDict[orderNumber][0]
        strategynamesymbol=self.orderIdStrategyDict[orderNumber][1]

        print strategyname,strategynamesymbol
        log(strategyname)
        log(strategynamesymbol)
        log('strategyNamesymbol')

        strategy1=self.strategyNameDict[strategyname]
        strategy1.onOrderEvent(event.dict_)


        log(orderNumber)
        log(eventFlavour)

        print orderNumber

    def processRequestId(self, event):

        print "processReuestId++++++++++++++++++++++++++++++++++++++++"
        print event.dict_.strategyName,event.dict_.requestId,event.dict_.symbol,event.dict_.side
        self.indexStrategyDict[event.dict_.requestId]=[event.dict_.strategyName,event.dict_.symbol,event.dict_.side]
        #sending oreder to 0
    def processTradeEvent(self,event):
        trade=event.dict_['data']
    def loadTick(self):
        pass
    def loadStrategy(self):



        s1=strategy(self)
        s2=strategy02(self)
        self.strategyTickDict['s1'] = s1.symbol
        self.strategyTickDict['s2'] = s2.symbol
        self.strategyNameDict[s1.strategyName]=s1
        self.strategyNameDict[s2.strategyName]=s2

        for s in s1.symbol:
            print s

            if s not in self.symbolRequest:
                self.symbolRequest.append(s)
                self.tickProcessDict[s]=[s1]
        print self.tickProcessDict

        for s in s2.symbol:
            if s  in self.symbolRequest:
                self.tickProcessDict[s].append(s2)

            else:
                self.symbolRequest.append(s)
                self.tickProcessDict[s]=[s2]




        print self.strategyTickDict
        print 'symbol:request'
        print self.symbolRequest
        print self.tickProcessDict

        # s2=strategy02(self)


    def loadSetting(self):
        """读取策略配置"""
        with open(self.settingfilePath) as f:
            l = json.load(f)

            for setting in l:
                self.loadStrategy(setting)



    def callStrategyFunc(self, strategy, func, params=None):
        """调用策略的函数，若触发异常则捕捉"""
        try:
            if params:
                func(params)
            else:
                func()
        except Exception:
            # 停止策略，修改状态为未初始化
            strategy.trading = False
            strategy.inited = False

            # 发出日志
            # content = '\n'.join([u'策略%s触发异常已停止' % strategy.name,
            #                      traceback.format_exc()])
            # self.writeCtaLog(content)

        #self.loadSyncData()

class barG(object):
    def __init__(self,onBar,xmin=0,onXminBar=None):
        self.lasttick=None
        self.vwap=0
    def getminbar(self,tick):
        if self.lasttick==None:
            self.lasttick=tick
            self.vwap=tick.price*tick.vol+self.vwap


    #     return self.result

if __name__=="__main__":
    ee = eventEngine()
    tr1=tradeEngine(ee)
    d1 = dataEngine(ee)




















