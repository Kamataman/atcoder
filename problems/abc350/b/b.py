n,q=map(int,input().split())
t=list(map(int,input().split()))

tooths=[True]*n
for ti in t:
    ti-=1
    if tooths[ti]:
        tooths[ti]=False
    else:
        tooths[ti]=True
print(tooths.count(True))