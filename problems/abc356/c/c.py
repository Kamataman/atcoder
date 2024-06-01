n,m,k=map(int,input().split())
conb=[False]*(1<<n)
c=[],a=[],r=[]
for i in range(m):
    print(conb)
    line=input().split()
    c.append(int(line[0]))
    a.append(list(map(int,line[1:c+1])))
    r.append(line[-1])
    
for con in conb:
    for i in range(m):        
        if r[i]=='o':
            mask=0
            for ai in a:
                mask+=1<<(ai-1)
            if con
        elif r[i]=='x':
            conb[con]=False

print(conb)
ans=0
for con in conb:
    if con==True:
        ans+=1
print(ans)