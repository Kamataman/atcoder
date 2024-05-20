n,m=map(int,input().split())
a=list(map(int,input().split()))

edge=[]
for i in range(n):
    edge.append([])

for i in range(m):
    x,y=map(int,input().split())
    edge[x-1].append(y-1)

#print(edge)

#dp[i] i番目の町から出発したときに売れる金の最大価値
dp=[-(10**9)]*n
answer=-(10**9)
for i in range(n-1,-1,-1):
    for e in edge[i]:
        dp[i]=max(dp[i],dp[e],a[e])
    answer=max(answer,dp[i]-a[i])

#print(dp)
print(answer)
