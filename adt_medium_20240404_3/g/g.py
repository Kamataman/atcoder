n=int(input())
a=list(map(int,input().split()))

UPPER=2*10**5+1
memo=[0]*UPPER
for ai in a:
    for i in range(ai+1,UPPER):
        memo[i]+=1

count=0
for j in range(n):
     count+=memo[a[j]]*(n-memo[a[j]]-1)
     print(count)
print(count)