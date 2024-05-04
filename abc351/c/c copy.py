N=int(input())
a=list(map(int,input().split()))

row=[-1]*N
ind=0
for i in range(N):
    row[ind]=a.pop(0)
    ind+=1
    while True:
        if ind<=1:
            break
        elif row[ind-1]!=row[ind-2]:
            break
        else:
            row[ind-2]=row[ind-1]+1
            ind-=1
            
print(ind)