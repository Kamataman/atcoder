N=int(input())
a=list(map(int,input().split()))

row=[-1]*N
ind=0
for ai in a:
    row[ind]=ai
    ind+=1
    while ind>1:
        if row[ind-1]==row[ind-2]:
            row[ind-2]=row[ind-1]+1
            ind-=1
        else:
            break
            
print(ind)