h,w,n=map(int,input().split())
row=[-1]*h
col=[-1]*w
for i in range(n):
    ai,bi=map(int,input().split())
    row[ai-1]=i
    col[bi-1]=i
row=list(filter(lambda x: x!=-1,row))
col=list(filter(lambda x: x!=-1,col))

for i in range(n):
    print('{} {}'.format(row.index(i)+1,col.index(i)+1))
