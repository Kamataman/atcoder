n,x,y,z=map(int,input().split())

if x<y:
    if x<z<y:
        print('Yes')
        exit()
else:
    if y<z<x:
        print('Yes')
        exit()
print('No')
exit()