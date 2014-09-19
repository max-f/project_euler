def primelist(n):
    # this implements the sieve of eratosthenes

    # we need to quickly remove the first element of our 'list' 
    # hence use queues!
    from collections import deque
    all_numbers=deque()

    limit=n  #n must be even
    primes=list()
    primes.append(2)

    # the next number (3) is also prime
    all_numbers.append(True)
    print "Sieving..."
    k=0 # k will be the difference between last prime discovered and current number
    for i in range(1,(limit/2)-1):
        all_numbers.append(False)
        all_numbers.append(True)
    all_numbers.append(False)

    while True:
        # get the next number in queue and check if it is prime, according to
        # knowledge
        try: 
            t=all_numbers.popleft()
            if t==True:
                k=k+1
                last=primes.pop() #remind ourselves of the highest prime we know
                primes.append(last) # write it down again, since 'pop' pops it
                primes.append(last+k) #write the new prime
                print(last+k)
                # now update our knowledge: all multiples of the new prime are 
                # no primes
                i=1
                while i*(last+k) <= len(all_numbers):
                    all_numbers[i*(last+k)-1]=False
                    i=i+1
                # we discovered a new prime, so difference to it is 0
                k=0
            else:
                # we didn't discover a new prime, so next number has higher
                # difference to last prime
                k=k+1
        #if queue is empty, we are done
        except:
                print "Done!"
                return primes

#returns list of strings containing only 1,3,7,9 of length in (a,b)
def candidates(a,b):
    l=['']
    i=0
    m=[]
    while i < b+1:
        l=extend(l)
        i=i+1
        if i in range(a,b+1):
            m.extend(l)
    return m
        
def extend(l):
    m=[]
    for x in l:
        for y in ['1','3','7','9']:
            m.append(x+y)
    return m

def rotate(s,i):
    d=len(s)
    t=s[i:]+s[:i]
    r=""
    for x in t:
        r=r+x
    return int(r)

primes = primelist(10**6)
low_primes = ['2','3','5','7']
#list of strings of numbers containing only 1,3,7,9 of length between 2 and 6
#Note that circular primes must be of this form!
candidates = candidates(2,6) 
print "The following numbers are circular primes:"
c=0
for p in low_primes + candidates:
    l=len(p) #number of digits of p
    t=[True]*l
    for i in range(0,l):
        t[i]= rotate(p,i) in primes
    if all(t):
        print int(p)
        c=c+1
print "Number of circular primes is:"
print c
