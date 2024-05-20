from atcoder import dsu
import itertools
import operator

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]

lim=w
def xy2int(x,y):
    return y*lim+x
def int2xy(n):
    return (n%lim,n//lim)

moves=[(0,1),(1,0),(-1,0),(0,-1)]

# 周囲に磁石があるか否か
isAroudMag=[[False]*w for _ in range(h)]
for pos in itertools.product(range(w),range(h)):
    for move in moves:
        moved=tuple(map(operator.add,pos,move))
        if 0<=moved[0]<w and 0<=moved[1]<h and s[moved[1]][moved[0]]=='#':
            isAroudMag[pos[1]][pos[0]]=True
            break

# 相互に行き来可能なグループを作成
uf=dsu.DSU(h*w)
for x,y in itertools.product(range(w),range(h)):
    if s[y][x]!='#':
        for dx,dy in moves:
            xdx,ydy=x+dx,y+dy
            if 0<=xdx<w and 0<=ydy<h and not isAroudMag[y][x] and not isAroudMag[ydy][xdx]:
                    uf.merge(xy2int(x,y),xy2int(xdx,ydy))

# groupのleaderをキーにサイズを格納
count={}
for group in uf.groups():
    leader=uf.leader(group[0])
    count[leader]=uf.size(leader)

# 周囲が磁石のマスについて周りのgroupにサイズを１加算
for x,y in itertools.product(range(w),range(h)):
    if s[y][x]!='#' and isAroudMag[y][x]:
        leaders=set()
        for dx,dy in moves:
            xdx,ydy=x+dx,y+dy
            if 0<=xdx<w and 0<=ydy<h and s[ydy][xdx]!='#' and not isAroudMag[ydy][xdx]:
                leaders.add(uf.leader(xy2int(xdx,ydy)))
        for leader in leaders:
            count[leader]+=1
            
print(max(count.values()))