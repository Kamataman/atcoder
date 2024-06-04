n,k=map(int,input().split())
a=list(map(int,input().split()))
t=sorted(list(set(a)))
ans=k*(k+1)//2
for ti in t:
    if ti<=k:
        ans-=ti
print(ans)