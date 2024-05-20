def function(n,a,s,t):
    for i in range(n-1):
        a[i+1]+=a[i]//s[i]*t[i]
    return a[n-1]


if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    t=[]
    for i in range(n-1):
        _s,_t=map(int,input().split())
        s.append(_s)
        t.append(_t)

    print(function(n,a,s,t))