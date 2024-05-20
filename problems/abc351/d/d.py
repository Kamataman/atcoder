from collections import deque

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]

maxfree=0
moves=[[0,1],[1,0],[-1,0],[0,-1]]
for i in range(h):
    for j in range(w):
        q=deque()
        check=[[False]*w for _ in range(h)]
        if s[i][j]!='#':
            free=0
            q.append([i,j])
            dist=[[-1]*w for _ in range(h)]
            dist[i][j]=1
            while(len(q)):
                nowi,nowj=q.popleft()
                free+=1
                # print(i,j,nowi,nowj,free)
                tempq=[]
                for move in moves:
                    di=nowi+move[0]
                    dj=nowj+move[1]
                    if 0<=di<h and 0<=dj<w:
                        if s[di][dj]=='#':
                            tempq=[]
                            break
                        else:
                            tempq.append([di,dj])
                if len(tempq)>0:
                    check[nowi][nowj]=True
                for t in tempq:
                    if check[t[0]][t[1]]==False:
                        if dist[t[0]][t[1]]==-1:
                            dist[t[0]][t[1]]=dist[nowi][nowj]+1
                            q.append(t)
            maxfree=max(maxfree,free)
print(maxfree)