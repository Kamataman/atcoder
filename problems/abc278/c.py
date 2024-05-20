n,q=map(int,input().split())

follow={}
for i in range(n):
    follow[i]=set()

for i in range(q):
    t,a,b=map(int,input().split())
    a=a-1
    b=b-1

    if t==1:
        follow[a].add(b)
    elif t==2:
        if b in follow[a]:
            follow[a].remove(b)
    elif t==3:
        if (b in follow[a]) & (a in follow[b]):
            print('Yes')
        else:
            print('No')        
