x1,z1=map(int,input().split(' '))
x2,z2=map(int,input().split(' '))
x3,z3=map(int,input().split(' '))
if (x1==x2 and x2==x3) or(z1==z2 and z2==z3):
    print("yes")
else:
    print("no")
