import math
l=math.factorial(100)
d=str(l)
s=[int(d[i]) for i in range(len(d))]
print sum(s)
