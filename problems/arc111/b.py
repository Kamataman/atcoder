n=int(input())
a=[0]*n
b=[0]*n
count=0
for i in range(n):
    a[i],b[i]=map(int,input().split())
    if a[i]==b[i]:
        count+=1

colors=set(a+b)

if len(colors)>=n:
    print(n)
else:
    if count>=len(colors)/2:
        print(len(colors)-count)
    else:
        print(len(colors))
