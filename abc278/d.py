n=int(input())
a=list(map(int,input().split()))
q=int(input())

for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        for j in range(n):
            a[j]=query[1]
    elif query[0]==2:
        a[query[1]-1]=a[query[1]-1]+query[2]
    elif query[0]==3:
        print(a[query[1]-1])
    
    # print('a : ',a)
    