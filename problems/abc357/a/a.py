n,m=map(int,input().split())
h=list(map(int,input().split()))
ans=0
for i in range(n):
    m-=h[i]
    if m<0:
        print(i)
        exit()
print(n)