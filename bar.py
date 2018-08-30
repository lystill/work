

import copy

class ba1r(object):
    def __init__(self,min):
        self.bar=None
        self.barE=None
        self.barElist=[]
        self.min=min
        self.barxminElist=[]
        self.onBar=None
        self.lastTick=None
    def updateTick(self,tick):
        if self.bar==None:
            self.bar=barData()
            self.bar.high=tick.price
            self.bar.close=tick.price

            self.bar.open=tick.price
            self.bar.low=tick.price
            self.bar.vol=tick.size


            self.bar.time=tick.time
        else:
            if int(tick.time[3:5])==int(self.bar.time[3:5]):

                self.bar.high=max(self.bar.high,tick.price)
                self.bar.low=min(self.bar.low,tick.price)
                self.bar.close=tick.price
                self.bar.vol=int(self.bar.vol)+int(tick.size)
            else:
                self.barE = copy.copy(self.bar)

                self.barElist.append(self.barE)

                self.bar.time=tick.time

                self.bar.high = tick.price
                self.bar.close = tick.price

                self.bar.open = tick.price
                self.bar.low = tick.price
                self.bar.vol = tick.size









class barData():
    def __init__(self):
        self.time=''
        self.symbol=''
        self.price=0.0


        self.high=0.0
        self.low=0.0
        self.open=0.0
        self.close=0.0
        self.vol=0
class tickData():
    def __init__(self):
        self.symbol=''
        self.price=0.0

        self.time=''
        self.size=0

class bar02(object):
    def __init__(self,min):
        self.bar=None
        self.barE=None
        self.barElist=[]
        self.min=min
        self.barStrat=False


        self.onBar=None
        self.lastTick=None
    def updateTick(self,tick):
        #chu shi hua
        if self.bar==None:
            self.bar=barData()
            self.bar.high=tick.price
            self.bar.close=tick.price

            self.bar.open=tick.price
            self.bar.low=tick.price
            self.bar.vol=tick.size


            self.bar.time=tick.time
        else:
            # self.barStrat = False
            if int(tick.time[3:5])%self.min!=0 :
                self.barStrat = False
                self.bar.high=max(self.bar.high,tick.price)
                self.bar.low=min(self.bar.low,tick.price)
                self.bar.close=tick.price
                self.bar.vol=int(self.bar.vol)+int(tick.size)

            elif int(tick.time[3:5])%self.min==0:
                if self.barStrat==False:
                    print int(tick.time[3:5])%self.min,'!!!!!!!!!!!!!!!!'

                    self.barE = copy.copy(self.bar)
                    print self.barE.time

                    self.barElist.append(self.barE)
                    #ti jiao zou wan kxian

                    self.bar.time=tick.time
                    self.bar.open=tick.price

                    self.bar.high = tick.price
                    self.bar.close = tick.price
                    self.bar.low=tick.price
                    self.bar.vol=tick.size
                    self.barStrat=True
                else:
                    self.bar.high = max(self.bar.high, tick.price)
                    self.bar.low = min(self.bar.low, tick.price)
                    self.bar.close = tick.price
                    self.bar.vol = int(self.bar.vol) + int(tick.size)

class bar(object):
    def __init__(self,onBar,symbol,min=0):
        self.bar=None
        self.symbol=symbol
        self.barCount=0
        self.barE=None
        self.barElist=[]
        self.min=min
        self.barStrat=False
        #x min bar nei 1  min
        self.newBar=False

        self.onBar=onBar
        self.lastTick=None
        self.onInit=False
    def updateTick(self,tick):

        #chu shi hua..1min
        if self.min==1:

            if self.bar == None:

                self.bar = barData()

                print self.bar.symbol,'bar data //////bar.symbol'
                self.bar.high = tick.price
                self.bar.close = tick.price

                self.bar.open = tick.price
                self.bar.low = tick.price
                self.bar.vol = tick.size

                self.bar.time = tick.time
            else:
                if int(tick.time[3:5]) == int(self.bar.time[3:5]):

                    self.bar.high = max(self.bar.high, tick.price)
                    self.bar.low = min(self.bar.low, tick.price)
                    self.bar.close = tick.price
                    self.bar.vol = int(self.bar.vol) + int(tick.size)
                else:
                    self.barStrat = True
                    self.newBar=True

                    self.barE = copy.copy(self.bar)

                    self.barElist.append(self.barE)
                    print self.newBar, "newBar...."
                    if self.onInit==False:
                        self.onBar(self)
                    print "onbar"

                    self.bar.time = tick.time

                    self.bar.high = tick.price
                    self.bar.close = tick.price

                    self.bar.open = tick.price
                    self.bar.low = tick.price
                    self.bar.vol = tick.size
                    self.barStrat = False
                    self.barCount=self.barCount+1
                    self.newBar=False
         #min>1
        else:
            if self.bar==None:


                self.bar=barData()

                self.bar.high=tick.price
                self.bar.close=tick.price

                self.bar.open=tick.price
                self.bar.low=tick.price
                self.bar.vol=tick.size


                self.bar.time=tick.time
            else:
                # self.barStrat = FalseR
                if int(tick.time[3:5])%self.min!=0 :
                    self.barStrat = False
                    self.bar.high=max(self.bar.high,tick.price)
                    self.bar.low=min(self.bar.low,tick.price)
                    self.bar.close=tick.price
                    self.bar.vol=int(self.bar.vol)+int(tick.size)

                elif int(tick.time[3:5])%self.min==0:
                    if self.barStrat==False:
                        if self.barCount==0:
                            self.barCount=self.barCount+1
                        #fen zhong kaishi zai zheng shu shijian


                        else:
                            self.newBar=True


                            self.barE = copy.copy(self.bar)
                            print self.barE.time

                            self.barElist.append(self.barE)
                            self.barCount=self.barCount+1
                            print self.newBar, "newBar....",self.bar.symbol
                            self.onBar(self)
                            print "onbar"

                        #ti jiao zou wan kxian

                        self.bar.time=tick.time
                        self.bar.open=tick.price

                        self.bar.high = tick.price
                        self.bar.close = tick.price
                        self.bar.low=tick.price
                        self.bar.vol=tick.size

                        #!!!!!!!!!push bar data
                        self.barStrat=True

                        self.newBar=False
                    else:
                        self.bar.high = max(self.bar.high, tick.price)
                        self.bar.low = min(self.bar.low, tick.price)
                        self.bar.close = tick.price
                        self.bar.vol = int(self.bar.vol) + int(tick.size)


