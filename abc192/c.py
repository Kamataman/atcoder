n,k=map(int,input().split())

def g1(x):
    if x==0:
        return 0
    a=[]
    while x>=1:
        a.append(str(x%10))
        x=x//10
#    a.append(str(x))
    a.sort(reverse=True)
    return(int(''.join(a)))

def g2(x):
    if x==0:
        return 0
    a=[]
    while x>=1:
        a.append(str(x%10))
        x=x//10
#    a.append(str(x))
    a.sort(reverse=False)
    return(int(''.join(a)))

def f(x):
    return g1(x)-g2(x)


ai=n
for i in range(k):
    ai=f(ai)
print(ai)
'''
print(g1(1000000000))
print(g2(1000000000))
'''