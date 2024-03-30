n=int(input())
t=[0]*n
x=[0]*n
y=[0]*n

for i in range(n):
    t[i],x[i],y[i]=map(int,input().split())

pos_x=0
pos_y=0
pos_t=0

for i in range(n):
    dist=abs(x[i]-pos_x)+abs(y[i]-pos_y)
    d_time=t[i]-pos_t
    if dist>d_time or dist%2!=d_time%2:
        print('No')
        exit()
    pos_x=x[i]
    pos_y=y[i]
    pos_t=t[i]

print('Yes')