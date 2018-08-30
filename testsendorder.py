
import httplib,time,urllib,requests



def sendhttp(url):
    conn = httplib.HTTPConnection('localhost',33555)
    #http://127.0.0.1:8080/Register?symbol=%s&feedtype=L2
    conn.request('GET',url)
    httpres = conn.getresponse()
    print httpres.status, httpres.reason,httpres.read()
    return  httpres.read()

    conn.close()
def sendorder1():

    url = 'http://localhost:8080/ExecuteOrder?limitprice =80&ordername=CHX Buy CHIXXETRA Limit DAY&shares=100&symbol=BMW.DE'
    urllib.urlopen(url)

def sendOrder():
    # sendurl ='/ExecuteOrder?symbol=2768.JP&limitprice=300&ordername=JAPN Buy TSE Limit DAY&shares=100'
    sendurl='/ExecuteOrder?limitprice =80&ordername=CHX Buy CHIXXETRA Limit DAY&shares=100&symbol=BMW.DE'
    parm2={'symbol': '2768.JP', 'limitprice': 335.00,'ordername':'JAPN Buy TSE Limit DAY','shares':200}
    sendrul2='limitprice=80&ordername=CHXE Buy CHIXXETRA Limit DAY&shares=100&symbol=BMW.DE'
    parm={'symbol':'BMW.DE','limitprice':89.2,'ordername':'CHXE%20Buy%20CHIXXETRA%20Limit%20DAY','shares':200}
    parm1 = {'symbol': 'BMW.DE', 'limitprice':'89.2', 'ordername': "CHXE Buy CHIXXETRA Limit DAY", 'shares':' 200'}



    try:
        params = urllib.urlencode(parm)
        # headers = {"Content-type": "application/x-www-form-urlencoded"
        headers = {'User-agent': 'agent', 'Accept': 'application/json'}
        params1={'symbol': '2768.JP', 'limitprice': '300.20','ordername':'JAPN Buy TSE Limit DAY','shares':'200'}
        #     , "Accept": "text/plain"}
        print params

        httpClient = httplib.HTTPConnection("localhost", 33555)
        httpClient.request("POST",  '/ExecuteOrder?',sendrul2,headers)
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()



    # sendurl='/SetOutput?symbol=ZVZZT.NQ&feedtype=L1&output=bykey&status=on'/ExecuteOrder?limitprice=80&ordername=CHXE Buy CHIXXET
    #/ExecuteOrder?limitprice=80&ordername=CHXE Buy CHIXXET
    # sendhttp(http://localhost:8080/ExecuteOrder?symbol=2768.JP&limitprice=300&ordername=JAPN Buy TSE Limit DAY&shares=100)
def sendorder2():
    res=requests.get('http://localhost:33555/ExecuteOrder?limitprice=80&ordername=CHXE Buy CHIXXETRA Limit DAY&shares=100&symbol=BMW.DE')

if __name__=="__main__":
    # symbol='2768.JP'
    # price='300'
    # gateway='JAPN Buy TSE Limit DAY'
    # size='100'
    # # sendOrder(symbol,price,gateway,size)
    # # URL='/ExecuteOrder?symbol=2768.JP&limitprice=300&ordername=JAPN Buy TSE Limit DAY&shares=100'
    # # sendhttp(URL)
    # sendOrder()
    # # sendhttp('/ExecuteOrder?limitprice =80&ordername=CHX Buy CHIXXETRA Limit DAY&shares=100&symbol=BMW.DE')
    # # sendorder1()
    # # for i in range(3):
    # #
    # #     sendorder2()'CHXE%20Buy%20CHIXXETRA%20Limit%20DAY
    # # sendorder1()
    #
    # sendhttp('/GetOpenOrders?user=YI033')
    # #YI033___02000044M276196100000
    # sendhttp('/GetOrderState?ordernumber=YI033___02000044M276196100000')
    urlbz=sendhttp('/ExecuteOrder?limitprice=89.2&ordername=BVMF%20Sell->Short%20BOVESPA%20Limit%20DAY&shares=100&symbol=VALE3.BZ')
    # s=sendhttp('/ExecuteOrder?limitprice=89.2&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE')
    for i in range(10):
        print i

        s2=sendhttp(urlbz)

