a,b=input().split()
hannin=['1','2','3']
if a==b:
    print('-1')
else:
    hannin.remove(a)
    hannin.remove(b)
    print(hannin[0])