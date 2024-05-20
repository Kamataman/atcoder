h,w=map(int,input().split())
a=[]
for i in range(h):
    a.append(list(input()))
n=int(input())
r=[0]*n
c=[0]*n
e=[0]*n
potion={}
for i in range(n):
    r[i],c[i],e[i]=map(int,input().split())
    potion[str(r[i]-1)+'.'+str(c[i]-1)]=e[i]

memo=[]
for i in range(h):
    memo.append([0]*w)


def next(i,j,eng):
    # print(i+1,j+1,eng)
    # Goal
    if a[i][j]=='T':
        return True

    if i+1<h and a[i+1][j]!='#':
        if next(i+1,j,eng-1):
            return True
    # right
    if j+1<w and a[i][j+1]!='#':
        if next(i,j+1,eng-1):
            return True
    # up
    if i-1>=0 and a[i-1][j]!='#':
        if next(i-1,j,eng-1):
            return True
    # left
    if j-1>=0 and a[i][j-1]!='#':
        if next(i,j-1,eng-1):
            return True

for i in range(h):
    for j in range(w):
        if a[i][j]=='S':
            if next(i,j,0):
                print('Yes')
                exit()
print('No')