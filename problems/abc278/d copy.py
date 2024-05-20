n=int(input())
a=list(map(int,input().split()))
q=int(input())

base=0
diff={}
for i in range(n):
    diff[i+1]=a[i]

for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        base=query[1]
        diff={}
    elif query[0]==2:
        if query[1] in diff:
            diff[query[1]]=diff[query[1]]+query[2]
        else:
            diff[query[1]]=query[2]
    elif query[0]==3:
        if query[1] in diff:
            print(base+diff[query[1]])
        else:
            print(base)
    
    print('diff : ',diff)
    