n=int(input())
a=list(map(int,input().split()))
a.sort()

# 累積和の作成
MAX=10**6
cumsum=[0]*MAX
for ai in a:
    cumsum[ai]+=1
for i in range(1,MAX):
    cumsum[i]+=cumsum[i-1]
    
ans=0
for i in range(n-1):
    ans+=sum(a[i+1:])//a[i]
print(ans)