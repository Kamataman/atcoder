n,m=map(int,input().split())

count=0
for i in range(60):
    if m>>i & 1:
        syo=(n//(2**(i+1)))*(2**i)
        amari=n%(2**(i+1))-(2**i-1)
        if amari<0:
            amari=0
        count+=syo+amari
print(count%998244353)