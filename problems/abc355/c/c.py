n,t=map(int,input().split())
a=list(map(int,input().split()))

bingo=[t+1]*(n*n)

for i in range(t):
    bingo[a[i]-1]=i+1

# yoko
minTurn=t+1
for i in range(n):
    maxTurn=0
    for j in range(n):
        maxTurn=max(maxTurn,bingo[n*i+j])
    minTurn=min(minTurn,maxTurn)

# tate
for j in range(n):
    maxTurn=0
    for i in range(n):
        maxTurn=max(maxTurn,bingo[n*i+j])
    minTurn=min(minTurn,maxTurn)

# naname
maxTurn=0
for i in range(n):
    maxTurn=max(maxTurn,bingo[n*i+i])
minTurn=min(minTurn,maxTurn)

maxTurn=0
for i in range(n):
    maxTurn=max(maxTurn,bingo[n*i+(n-i-1)%n])
minTurn=min(minTurn,maxTurn)

print('-1' if minTurn==t+1 else minTurn)

