h,w,q=map(int,input().split())
queries=[list(map(lambda x: x-1,map(int,input().split()))) for _ in range(q)]

board=[[1]*w for _ in range(h)]

for r,c in queries:
    if board[r][c]:
        board[r][c]=0
    else:
        dircs=[(-1,0),(1,0),(0,-1),(0,1)]
        for dirc in dircs:
            count=1
            dr=r+count*dirc[0]
            dc=c+count*dirc[1]
            while 0<=dr<h and 0<=dc<w:
                if board[dr][dc]:
                    board[dr][dc]=0
                    break
                count+=1
                dr=r+count*dirc[0]
                dc=c+count*dirc[1]
    # for _ in board:
    #     print(_)
    # print()
sum=0
for i in range(h):
    for j in range(w):
        if board[i][j]:
            sum+=1
print(sum)