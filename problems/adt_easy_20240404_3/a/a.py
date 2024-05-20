v,a,b,c=map(int,input().split())

while True:
    if v>=a:
        v-=a
    else:
        print('F')
        exit()
    if v>=b:
        v-=b
    else:
        print('M')
        exit()
    if v>=c:
        v-=c
    else:
        print('T')
        exit()