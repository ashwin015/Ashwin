s=int(input())
f=0
for i in range(2,s//2+1):
    if(s%i==0):
        f=f+1
if(f<=0):
    print('yes')
else:
    print('no')
