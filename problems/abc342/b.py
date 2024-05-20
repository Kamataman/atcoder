n=int(input())
p=list(map(int,input().split()))
q=int(input())
a=[]
b=[]
for i in range(q):
    a_t,b_t=map(int,input().split())
    a.append(a_t)
    b.append(b_t)

for i in range(q):
    if p.index(a[i])<p.index(b[i]):
        print(a[i])
    else:
        print(b[i])




