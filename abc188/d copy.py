n,C=map(int,input().split())

event=[]
for i in range(n):
    a,b,c=map(int,input().split())
    event.append((a,c))
    event.append((b+1,-c))
event.sort()
#print(event)

day=1
dailycost=0
totalcost=0
for x,y in event:
    if day!=x:
        totalcost+=min(dailycost,C)*(x-day)
        day=x
    dailycost+=y
print(totalcost)