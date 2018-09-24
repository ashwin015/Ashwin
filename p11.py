x1,z1=map(int,input("Enter 1st line").split(' '))
x2,z2=map(int,input("Enter 2nd line").split(' '))
x3,z3=map(int,input("Enter 3rd line").split(' '))
if (x1==x2 and x2==x3) or(z1==z2 and z2==z3):
    print("yes")
else:
    print("no")
