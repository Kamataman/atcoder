n,k=map(int,input().split())
h=list(map(int,input().split()))

dp=[float('INF')]*n
dp[0]=0
for i in range(1,n):
    for j in range(1,min(k+1,i+1)):
        cost=dp[i-j]+abs(h[i]-h[i-j])
        dp[i]=min(dp[i],cost)
# print(dp)
print(dp[n-1])