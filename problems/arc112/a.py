t=int(input())
l=[0]*t
r=[0]*t
for i in range(t):
    l[i],r[i]=map(int,input().split())

for i in range(t):
    count=0
    for c in range(r[i]-l[i]+1):
        count+=r[i]-l[i]-c+1
    print(count)