n=int(input())
h=list(map(int,input().split()))
dp=[0]*n
dp[0]=0
dp[1]=abs(h[0]-h[1])
for i in range(2,n):
    cost1=dp[i-1]+abs(h[i]-h[i-1])
    cost2=dp[i-2]+abs(h[i]-h[i-2])
    if cost1<cost2:
        dp[i]=cost1
    else:
        dp[i]=cost2

# print(dp)
print(dp[n-1])