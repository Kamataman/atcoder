n=int(input())
a=list(map(lambda x:x-1,map(int,input().split())))

# print(a)
address=[0]*n
for i,ai in enumerate(a):
    address[ai]=i

steps=[]
for i in range(n):
    if i!=a[i]:
        steps.append([i+1,address[i]+1])
        a[address[i]]=a[i]
        address[a[i]]=address[i]
    
print(len(steps))
for step in steps:
    print(' '.join(map(str,step)))