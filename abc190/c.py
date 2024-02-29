n,m=map(int,input().split())
a=[0]*m
b=[0]*m
for i in range(m):
    ta,tb=map(int,input().split())
    a[i]=ta
    b[i]=tb
k=int(input())
c=[0]*k
d=[0]*k
for i in range(k):
    tc,td=map(int,input().split())
    c[i]=tc
    d[i]=td

x=[]
for i in range(2**k):
    tmp=[]
    for j in range(k):
        if (i >> j) & 1:
            tmp.append(d[j])
        else:
            tmp.append(c[j])
    x.append(tmp)

ans=0
for pattern in x:
    count=0
    for i in range(m):
        if a[i] in pattern and b[i] in pattern:
            count+=1
    ans=max(ans,count)

print(ans)