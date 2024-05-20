import math

n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i],y[i]=map(int,input().split())

for i in range(n):
    max_i=0
    max_dist=0
    for j in range(n):
        dist=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
        if dist>max_dist:
            max_i=j
            max_dist=dist   
    print(max_i+1)        
    