import numpy as np
from datetime import datetime
from collections import OrderedDict

from sendhttp import *
from dataEngine import *
from threading import  Thread
import xml.etree.ElementTree as ET
import traceback
from p8Function import *
import json
class sendOrderThread(Thread):
    def __init__(self,symbol,side,price,gateway, size,strategyName,eventEngine):
        Thread.__init__(self)
        self.symbol=symbol
        self.price=price
        self.side=side
        self.gateway=gateway
        self.size=size
        self.result=0
        self.eventEngine=eventEngine
        self.strategyName=strategyName
    def run(self):
        #'/ExecuteOrder?limitprice=89.2&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE'
        sendurl = '/ExecuteOrder?symbol=%s&limitprice=%s&ordername=%s&shares=%s'%(self.symbol, self.price, self.gateway, self.size)

        print sendurl
        r=sendhttp(sendurl)
        root = ET.fromstring(r)

        id = root[0].text
        self.result=id
        # self.eventEgine.put()
        print id,'dddddddddddddddddddddddddddddddddddddd'
        sid=strategyRequestId()

        sid.strategyName=self.strategyName
        sid.requestId=id
        sid.symbol=self.symbol
        sid.side=self.side

        # print 'sid.strategyname',sid.strategyName,sid.requestId
        eventid=Event()
        eventid.type_ = 'EVENT_requestId'
        eventid.dict_ = sid
        # print event.dict_.requestId,'here id'
        eventid.puttime=datetime.now()
        self.eventEngine.put(eventid)