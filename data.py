import os, sys
import time
import datetime

t = datetime.datetime.now().strftime('%Y%m%d')
i = 0

print "wen"
os.chdir('d:\\data')
if not os.path.exists(t):
    os.makedirs(t)
    print '%s is not exits' % t
os.chdir(t)
os.makedirs('s')

# os.makedirs(t)
while 1:
    fo = open('d:\\' + str(t) + '.txt', 'a+')
    fo.write(str(i) + '\n')
    fo.write(str(datetime.datetime.now()) + '\n')
    i = i + 1
    print i
    time.sleep(1)
    fo.close()

# with open('/path/to/file', 'r') as f:
#    print f.read()
#    try:
#    f = open('/path/to/file', 'r')
#    print f.read()
# finally:
#    if f:
#        f.close()
