import numpy
import copy
n=3

a=[list(map(int,input().split())) for _ in range(n)]
#hand -1: empty 0: t 1: a
def check(board,hand):
    
    for i in range(n):
        # row
        if board[i][0]==board[i][1]==board[i][2]==0:
            return 0
        elif board[i][0]==board[i][1]==board[i][2]==1:
            return 1
        # col
        if board[0][i]==board[1][i]==board[2][i]==0:
            return 0
        elif board[0][i]==board[1][i]==board[2][i]==1:
            return 1
    # cross
    if board[0][0]==board[1][1]==board[2][2]==0:
        return 0
    elif board[0][0]==board[1][1]==board[2][2]==1:
        return 1
    if board[0][2]==board[1][1]==board[2][0]==0:
        return 0
    elif board[0][2]==board[1][1]==board[2][0]==1:
        return 1

    # score
    if -1 not in numpy.array(board):
        score={0:0,1:0}
        for i in range(n):
            for j in range(n):
                if board[i][j]==0:
                    score[0]+=a[i][j]
                elif board[i][j]==1:
                    score[1]+=a[i][j]
        if score[0]>score[1]:
            return 0
        else:
            return 1

    # not end
    for i in range(n):
        for j in range(n):
            if board[i][j]==-1:
                nextBoard=copy.deepcopy(board)
                nextBoard[i][j]=hand
                if check(nextBoard,(hand+1)%2)==hand:
                    return hand
    return (hand+1)%2

startBoard=[[-1]*3 for _ in range(n)]
result=check(startBoard,0)
if result==0:
    print('Takahashi')
elif result==1:
    print('Aoki')