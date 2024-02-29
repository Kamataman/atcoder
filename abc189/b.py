n,x=map(int,input().split())
al=0
for i in range(n):
    v,p=map(int,input().split())
    al+=v*p
    if al>x*100:
        print(i+1)
        exit()

print(-1)