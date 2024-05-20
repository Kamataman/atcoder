r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
map=[list(input()) for _ in range(r)]

from collections import deque
q=deque()
dist=[[-1]*c for _ in range(r)]
q.append([sy-1,sx-1])
dist[sy-1][sx-1]=0

moves=[[1,0],[0,1],[-1,0],[0,-1]]
while len(q)>0:
    # for i in dist:
    #     print(i)
    now_r,now_c=q.popleft()
    for move in moves:
        moved_r=now_r+move[0]
        moved_c=now_c+move[1]
        if dist[moved_r][moved_c]==-1 and map[moved_r][moved_c]!='#':
            dist[moved_r][moved_c]=dist[now_r][now_c]+1
            q.append([moved_r,moved_c])
print(dist[gy-1][gx-1])