n,x=map(int,input().split())
p=list(map(int,input().split()))

for i,pi in enumerate(p):
    if pi==x:
        print(i+1)