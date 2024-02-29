n,q=map(int,input().split())

follow=set()

for i in range(q):
    t,a,b=map(int,input().split())
    a=a-1
    b=b-1

    if t==1:
        follow.add(a*n+b)
    elif t==2:
        if a*n+b in follow:
            follow.remove(a*n+b)
    elif t==3:
        if (a*n+b in follow) & (b*n+a in follow):
            print('Yes')
        else:
            print('No')        
