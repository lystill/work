import urllib,urllib2,time
from  sendhttp import *
PORT=4413
eu=['BMW.DE','DAI.DE','BAS.DE','RNO.PA','DTE.DE','CS.PA','GLE.PA','BNP.PA','SAN.PA','BAYN.DE','FP.PA']
de=['BMW.DE','DAI.DE','BAS.DE','SAP.DE','BAYN.DE','TKA.DE','DTE.DE','LHA.DE','SIE.DE']
ny=['MMM.NY', 'AA.NY', 'AXP.NY', 'T.NY', 'BAC.NY', 'BA.NY', 'CAT.NY', 'CVX.NY',
               'CSCO.NY', 'DD.NY', 'XOM.NY', 'GE.NY', 'HPQ.NY', 'HD.NY', 'INTC.NY', 'IBM.NY',
               'JNJ.NY', 'JPM.NY', 'MCD.NY', 'MRK.NY', 'MSFT.NY', 'PFE.NY', 'PG.NY', 'KO.NY',
               'TRV.NY', 'UTX.NY', 'UNH.NY', 'V.NYZ', 'WMT.NY', 'DIS.NY']

cn=['N.CN','EAT.CN','MMJ.CN','MYM.CN']
hk=['3188.HK','0939.HK','2327.HK','0175.HK','2899.HK','1398.HK','3988.HK','0386.HK','0857.HK','0883.HK','2318.HK','2007.HK','0762.HK',
    '2628.HK','0836.HK','0992.HK','1928.HK','1088.HK','3328.HK']
jp=['8411.JP','8306.JP','6502.JP','7201.JP','5301.JP','6501.JP','6752.JP','8604.JP',
    '6702.JP','4755.JP','7201.JP','4689.JP','8308.JP','8601.JP','5020.JP','4005.JP',
    '7261.JP','3436.JP','9501.JP','2768.JP']
ol=['DNB.OL','MHG.OL','DNO.OL','STL.OL','GSF.OL']
lo=['BT.LO','LLOY.LO']
bz=['ABEV3.BZ',
'ALLL3.BZ',
'BBAS3.BZ',
'BBDC4.BZ',
'BBSE3.BZ',
'BRFS3.BZ',
'BRML3.BZ',
'BRPR3.BZ',
'BVMF3.BZ',
'CCRO3.BZ',
'CIEL3.BZ',
'CMIG4.BZ',
'CBZN3.BZ',
'CSNA3.BZ',
'ECOR3.BZ',
'ELET3.BZ',
'ESTC3.BZ',
'GFBZ3.BZ',
'GGBR4.BZ',
'GOLL4.BZ',
'HYPE3.BZ',
'ITBZ4.BZ',
'ITUB3.BZ',
'JBSS3.BZ',
'KROT3.BZ',
'LAME4.BZ',
'MRFG3.BZ',
'MULT3.BZ',
'PETR3.BZ',
'PETR4.BZ',
'QUAL3.BZ',
'SUZB5.BZ',
'TIMP3.BZ',
'VALE3.BZ',
'VALE5.BZ',
'USIM5.BZ',
'BRKM5.BZ',
'EMBR3.BZ',
'KLBN11.BZ',
'UGPA3.BZ']
stocklist=eu
url_L2='/Register?symbol=%s&feedtype=L2'
url_L1='/Register?symbol=%s&feedtype=L1'
url_TOS='/Register?symbol=%s&feedtype=TOS'
url_L1_Setuotput='/SetOutput?symbol=%s&feedtype=L1&output=%s&status=on'
url_TOS_Setuotput='/SetOutput?symbol=%s&feedtype=TOS&output=%s&status=on'
url_Deregister_TOS='/Register?symbol=%s&feedtype=TOS'
url_OSTAT_Setoutput='/SetOutput?region=%s&feedtype=OSTAT&output=%s&status=on'
url_ORDEREVENT_Setoutput='/SetOutput?region=%s&feedtype=ORDEREVENT&output=%s&status=on'
url_PAPIORDER_Setoutput='/SetOutput?region=%s&feedtype=PAPIORDER&output=%s&status=on'

def reqData(stocklist,port):
    for stock in stocklist:
        print stock
        sendhttp(url_Deregister_TOS%stock)
        sendhttp(url_TOS%stock)
        sendhttp(url_TOS_Setuotput%(stock,str(port)))
def reqOrderEvent(region,port):
    sendhttp(url_ORDEREVENT_Setoutput%(str(region),str(port)))
def reqOstat(region,port):
    sendhttp(url_OSTAT_Setoutput% (str(region), str(port)))
def reqPAPIORDER(region,port):
    sendhttp(url_PAPIORDER_Setoutput% (str(region), str(port)))
def reqEu():
    region=2
    reqOrderEvent(region, 4413)
    # reqOstat(region,4414)
    reqPAPIORDER(region, 4413)
    reqData(eu,4413)
    reqData(ol,4413)
    reqData(lo,4413)
def reqAs():
    region=3
    reqOrderEvent(region, 4413)
    # reqOstat(region,4414)
    reqPAPIORDER(region, 4413)
    reqData(jp, 4413)
    reqData(hk, 4413)
def reqAf():
    region=1
    reqOrderEvent(region, 4413)
    # reqOstat(region,4414)
    reqPAPIORDER(region, 4413)
    reqData(bz,4413)

if __name__=="__main__":
    reqEu()
    # reqAf()
    reqData(de,4413)
    # reqAs()
    # reqOrderEvent(2, 4415)
    # reqOstat(2,4416)
    # reqEu()
