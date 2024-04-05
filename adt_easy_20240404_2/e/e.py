h,w=map(int,input().split())
g=[]
for i in range(h):
    g.append(list(input()))


arrived=[]
for i in range(h):
    arrived.append([False]*w)

now_x=0
now_y=0

while True:
    # print(arrived)
    if arrived[now_y][now_x]:
        print('-1')
        exit()
    else:
        arrived[now_y][now_x]=True
    
    if g[now_y][now_x]=='U':
        if now_y==0:
            break
        else:
            now_y-=1
    elif g[now_y][now_x]=='D':
        if now_y==h-1:
            break
        else:
            now_y+=1
    elif g[now_y][now_x]=='L':
        if now_x==0:
            break
        else:
            now_x-=1
    elif g[now_y][now_x]=='R':
        if now_x==w-1:
            break
        else:
            now_x+=1

print('{} {}'.format(now_y+1,now_x+1))