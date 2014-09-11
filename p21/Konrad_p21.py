import math
        
        
# called with (n,[1]) returns a list (1, p, p, q, ...) of ordered prime divisors
# of n with multiplicities!
def get_divs(n,l):

    if n==2:
        l.append(2)
        return l
        
    for d in range(2,int(math.ceil(math.sqrt(n))+1)):
        if n % d==0:
            l.append(d)
            return get_divs(n/d, l)
    l.append(n)
    return l
    
# called with an ordered list, it returns pairs of values and counts
def combine(l):
    d=list() #list of pairs '(prime p, power of p in n)'
    y=l[0]
    c=0
    for x in l:
        if x==y:
            c=c+1
        else :
            d.append([y,c])
            y=x
            c=1
    d.append([y,c])
    return d

# called with a list of '(v, c)' pairs it returns all combinations of
# values, where v occurs up to c times
def proper_divs(d):
    a=[1] #list of divisors
    
    for p in d:
        b=list()
        for i in range(p[1]+1):
            b.extend([x*p[0]**i for x in a])
        a=b
    return a

def proper_divisor_sum(n):
    prime_divs=get_divs(n,[1]) #get prime decomp of n as ordered list
    prime_powers=combine(prime_divs) #get prime powers
    divs=proper_divs(prime_powers[1:]) #cut [1,1] and get all divisors
    divs.pop() #remove n, since n is not proper divisor of n
    return sum(divs)


#main loop
def main():
    k=list()
    for n in range(1,10001):
        p=proper_divisor_sum(n)
        #print p
        if n==proper_divisor_sum(p) and p != n: #try 'is not' instead of != :-D
            k.append(n)
    print k
    print sum(k)-1

main()
