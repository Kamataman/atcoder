n,m=map(int,input().split())
a,b=[0]*m,[0]*m
for i in range(m):
    a[i],b[i]=map(lambda x: x-1,map(int,input().split()))

from atcoder import dsu
uf=dsu.DSU(n)
for i in range(m):
    uf.merge(a[i],b[i])

# 全て友達なった場合のエッジ数
edges={}
for group in uf.groups():
    nodes=len(group)
    edges[uf.leader(group[0])]=nodes*(nodes-1)//2

# 既存のエッジを減算
for i in range(m):
    edges[uf.leader(a[i])]-=1

# エッジを合計
sum=0
for e in edges.values():
    sum+=e
print(sum)