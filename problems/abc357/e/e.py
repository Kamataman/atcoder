n=int(input())
a=list(map(int,input().split()))

seen=[False]*n
finished=[False]*n
def dfs(i):
    # if seen[i]:
        
    seen[i]=True
    dfs(a[i])
    finished[i]=True