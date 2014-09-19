import math

m= range(2540161)
l= [str(x) for x in m]

summe=0
for x in l:
    t= sum([math.factorial(int(a)) for a in x])
    if t==int(x):
        print x
        summe=summe+t
print "Summe ist "
print summe-1-2 #we don't want to count 1=1**5!
