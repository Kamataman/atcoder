import itertools

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

n,m=map(int,input().split())
k=[0]*m
c=[0]*m
a=[[] for _ in range(m)]

edges=[]

for i in range(m):
    k[i],c[i]=map(int,input().split())
    a[i]=list(map(lambda x: x-1,map(int,input().split())))
    # for conb in itertools.combinations(a[i],2):
    #     edge=list(conb)
    #     edge.append(c[i])
    for j in range(1,k[i]):
        edge=[a[i][0],a[i][j],c[i]]
        edges.append(edge)

edges=sorted(edges,key=lambda x: x[2])

uf=UnionFind(n)
cost=0
for edge in edges:
    if not uf.same(edge[0],edge[1]):
        uf.union(edge[0],edge[1])
        cost+=edge[2]

if uf.group_count()==1:
    print(cost)
else:
    print('-1')
