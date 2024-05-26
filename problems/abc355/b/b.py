n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c.sort()
f=False
for i in range(n+m-1):
    if c[i] in a and c[i+1] in a:
        print('Yes')
        exit()
print('No')