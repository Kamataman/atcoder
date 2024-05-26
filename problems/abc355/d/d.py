n=int(input())
l=[0]*n
r=[0]*n
t={}
for i in range(n):
    l[i],r[i]=map(int,input().split())
    t[l[i]]=t.get(l[i],0)+1
    t[r[i]+1]=t.get(r[i]+1,0)-1

# for i,k in enumerate(sorted(t.keys())):
#     print(k,t[k])

for i,k in enumerate(sorted(t.keys())):
    if i==0:
        beforeKey=k
    else:        
        t[k]+=t[beforeKey]
        beforeKey=k

d=[]
for k in t.keys():
    if t[k]==0:
        d.append(k)
for i in d:
    t.pop(i)
for i,k in enumerate(sorted(t.keys())):
    print(k,t[k])

count=0
for i,k in enumerate(sorted(t.keys())):
    if i==0:
        beforeValue=t[k]
    else:
        if t[k]>beforeValue:
            count+=t[k]-1
        beforeValue=t[k]

print(count)