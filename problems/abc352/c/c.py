n=int(input())
a=[0]*n
b=[0]*n

maxdiff=0
maxind=0
for i in range(n):
    a[i],b[i]=map(int,input().split())
    diff=b[i]-a[i]
    if diff>maxdiff:
        maxdiff=diff
        maxind=i

ans=b[maxind]
for i in range(n):
    if i!=maxind:
        ans+=a[i]

print(ans)