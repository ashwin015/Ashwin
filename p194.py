a1,a2 = input().split()
if a1=='P' and a2=='R' or a1=='R' and a2 == 'P' :
    print('P')
elif a1=='P' and a2=='S' or a1=='S' and a2=='P' :
    print('S')
elif a1=='S' and a2=='R' or a1=='R' and a2=='S' :
    print('R')
elif a1=='S' and a2=='S' :
    print('D')
elif a1=='P' and a2=='P' :
    print('D')
elif a1=='R' and a2=='R' :
    print('D')
