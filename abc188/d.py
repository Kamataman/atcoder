n,c=map(int,input().split())
a=[0]*n
b=[0]*n
c=[0]*n

dailycost={}

for i in range(n):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        if j in dailycost:
            dailycost[j]=dailycost[j]+c
        else:
            dailycost[j]=c

print(dailycost)

#ナイーブな方法
#メモリがあふれる
