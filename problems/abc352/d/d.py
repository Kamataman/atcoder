from sortedcontainers import SortedList

n,k=map(int,input().split())
p=list(map(int,input().split()))

place=[0]*n
for i,pi in enumerate(p):
    place[pi-1]=i

s =SortedList()
for i in range(k):
    s.add(place[i])

minidx=s[len(s)-1]-s[0]
for i in range(k,n):
    s.add(place[i])
    s.discard(place[i-k])
    minidx=min(minidx,s[len(s)-1]-s[0])

print(minidx)