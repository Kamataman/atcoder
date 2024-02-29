n,m=map(int,input().split())
a=list(map(int,input().split()))
gap=0
for i in range(len(a)-1):
    gap=min(gap,a[i+1]-a[i])
