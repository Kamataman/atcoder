import itertools

n,k=map(int,input().split())
t=[]
for i in range(n):
    t.append(list(map(int,input().split())))
'''
def permutation(arglist):
    print(arglist)
    if len(arglist)==1:
        return arglist
    else:
        ans=[]
        for i in arglist:
            popped=list(arglist)
            popped.pop(i)
            ans.append([i].extend(permutation(popped)))
        return ans
'''

count=0
for route in itertools.permutations(range(1,n)):
    routetime=0
    route=[0]+list(route)+[0]
    for i in range(1,len(route)):
        routetime+=t[route[i-1]][route[i]]
    if routetime==k:
        count+=1
print(count)
