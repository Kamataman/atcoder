import sys
sys.setrecursionlimit(100000)

n=int(input())

const=[]
for i in range(1,7):
    const.append(6**i)
for i in range(1,6):
    const.append(9**i)

const.sort()
#print(const)

def recursive(n,memo):
#    print(n)
    if n in memo:
        return memo[n]
    else:
        if n<6:
            return n
        else:
            res=100000
            for con in const:
                if n-con>=0:
                    res=min(res,recursive(n-con,memo)+1)
            memo[n]=res
            return memo[n]

print(recursive(n,{}))