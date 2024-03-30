a,b,c,d=map(int,input().split())

count=0
for i in range(101):
    if a<i and c<i and i<=b and i<=d:
       count+=1
print(count)