k=int(input())
c=list(map(int,input().split()))

import math
ans=0
s_count=sum(c)

dup_count=0
for i in range(26):
    if c[i]>1:
        dup_count+=c[i]-1

for i in range(1,k+1):
    ans+=math.perm(s_count,i)
    print(ans)
    ans-=dup_count*math.perm(s_count,i-1)
    print(ans)
    ans-=dup_count*(s_count-dup_count-1)*math.perm(s_count-du,i-2)
    print(ans)

print(ans%998244353)