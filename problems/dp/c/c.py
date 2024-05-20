n=int(input())
a=[0]*n
b=[0]*n
c=[0]*n

for i in range(n):
    a[i],b[i],c[i]=map(int,input().split())

# i日目にa,b,cを選んだ時の最大値を[a,b,c]でdpとする
dp=[[0,0,0] for _ in range(n)]

dp[0]=[a[0],b[0],c[0]]

for i in range(1,n):
    a_max=max(dp[i-1][1],dp[i-1][2])+a[i]
    b_max=max(dp[i-1][0],dp[i-1][2])+b[i]
    c_max=max(dp[i-1][0],dp[i-1][1])+c[i]
    dp[i]=[a_max,b_max,c_max]

# print(dp)
print(max(dp[n-1]))