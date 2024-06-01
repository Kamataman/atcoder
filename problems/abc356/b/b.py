n,m=map(int,input().split())
a=list(map(int,input().split()))
x=[list(map(int,input().split())) for _ in range(n)]

eiyo=[0]*m

for i in range(n):
    for j in range(m):
        eiyo[j]+=x[i][j]

for i in range(m):
    if a[i]>eiyo[i]:
        print('No')
        exit()
print('Yes')