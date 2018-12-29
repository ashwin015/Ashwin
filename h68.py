a=int(input())
p=input().split()
n=[]
for x in p:
    n.append(int(x))
print(n.index(min(n))+1,n.index(max(n))+1)
