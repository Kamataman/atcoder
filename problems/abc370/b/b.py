n=int(input())
a=[list(map(lambda x: x-1,map(int,input().split()))) for _ in range(n)]

now=0
for _ in range(n):
    if now>=_:
        now=a[now][_]
    else:
        now=a[_][now]
print(now+1)