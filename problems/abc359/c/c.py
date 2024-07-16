sx,sy=map(int,input().split())
tx,ty=map(int,input().split())

cost=abs(sy-ty)
dx=abs(sx-tx)
if dx>cost:
    cost+=dx//2
print(cost)
