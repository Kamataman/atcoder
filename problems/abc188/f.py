x,y=map(int,input().split())

#nからxに減らすときの最小操作回数
def solve(x,n,memo):
#    print((x,n))
    if n not in memo:
        if x>=n:
            return x-n
        else:
            if n%2==0:
                ret=min(solve(x,n//2,memo)+1,n-x)
            else:
                ret=min(solve(x,n+1,memo)+1,solve(x,n-1,memo)+1)
        memo[n]=ret
        return ret
    else:
        return memo[n]


print(solve(x,y,{}))