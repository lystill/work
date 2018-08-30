# -*- coding: utf-8 -*-
import httplib,time,datetime



def sendhttp(url):


    try:
        print 'start',datetime.datetime.now()
        conn = httplib.HTTPConnection('localhost',33555)
        # print '1', datetime.datetime.now()
        #http://127.0.0.1:8080/Register?symbol=%s&feedtype=L2

        conn.request('GET',url)
        # print '2', datetime.datetime.now()
        httpres = conn.getresponse()
        # print '3', datetime.datetime.now()
        # print httpres.status, httpres.reason
        z=httpres.read()
        # print '4', datetime.datetime.now()

    except Exception,e:
        print e
        return e
        z='Error'
    finally:
        print 'end', datetime.datetime.now()
        # print z
        return z
        if conn:
            conn.close()
 #


if __name__ == '__main__':
    url='/Register?symbol=AA.NY&feedtype=TOS'
    url_TOS_Setuotput = '/SetOutput?symbol=AA.NY&feedtype=TOS&output=4413&status=on'
    url1='/ExecuteOrder?limitprice=89&ordername=CHXE%20Buy%20CHIXXETRA%20Limit%20DAY&shares=100&symbol=BMW.DE'
    # z=sendhttp(url1)
    # # time.sleep(1)
    # print z
    z=sendhttp('')


