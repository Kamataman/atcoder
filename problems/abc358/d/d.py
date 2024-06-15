n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
ans=0
j=0
for i in range(n):
    if a[i]>=b[j]:
        ans+=a[i]
        j+=1
        if j>=m:
            print(ans)
            exit()
if j>=m:
    print(ans)
    exit()
else:
    print('-1')