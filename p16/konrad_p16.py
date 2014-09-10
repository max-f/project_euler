from collections import deque
import time

start = time.time()

def times2(r):
    c=0 # carry
    if r[0] >=5:
        r.appendleft(0)
    for i in range(len(r)-1,-1,-1):
        #print i
        if r[i]*2+c <=9:
            r[i]=r[i]*2+c
            c=0
        else:
            temp=r[i]
            r[i]=(r[i]*2+c) % 10
            c=(temp*2+c) // 10
    return r
            
l=deque(list())
l.append(1)

for k in range(1000):
    l=times2(l)
#print len(l)
#print l
#print sum(l)
print 'calculated %d in %d seconds' % (sum(l), time.time() - start)
