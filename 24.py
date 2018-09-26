ae=[]
n=int(input())
for i in range(1,n+1):
    sb=input()
    ae.append(sb)
ae.sort(key=len)
print(ae)
