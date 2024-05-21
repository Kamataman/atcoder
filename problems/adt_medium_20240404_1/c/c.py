edge=[3,1,4,1,5,9]
p,q=input().split()

pq=[p,q]
pq.sort()
dist=0
for i in range(ord(pq[0])-ord('A'),ord(pq[1])-ord('A')):
    dist+=edge[i]
print(dist)