import copy
n=int(input())
a=[]
for i in range(n):
    a.append(list(input()))

copied=copy.deepcopy(a)

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            copied[0][0]=a[i+1][j]
        elif i==0:
            copied[i][j]=a[i][j-1] 
        elif i==n-1 and j==n-1:
            copied[i][j]=a[i-1][j]
        elif i==n-1:
            copied[i][j]=a[i][j+1]
        elif j==0:
            copied[i][j]=a[i+1][j]
        elif j==n-1:
            copied[i][j]=a[i-1][j]

for i in range(n):
    print(''.join(copied[i]))