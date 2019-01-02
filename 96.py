import math
A,B,C=map(int,input().split(' '))
a=A
d=B
n=C
total = (n * (2 * a + (n - 1) * d)) / 2
print(math.floor(total))
