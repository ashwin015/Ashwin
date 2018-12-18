import math
e,s=map(int,input().split(' '))
n=e*s
if math.sqrt(n)==int(math.sqrt(n)):
    print ("Yes")
else:
    print ("No")
