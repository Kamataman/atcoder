n,a=map(int,input().split())
t=list(map(int,input().split()))

ans=0
for i in range(n):
    if ans<t[i]:
        ans=t[i]+a
    else:
        ans+=a
    print(ans)