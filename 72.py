n=input()
vo=set('aeiou')
vi=set('AEIOU')
if not vo.isdisjoint(n):
    print ("yes")
elif not vi.isdisjoint(n):
    print ("yes")
else:
    print ("no")
