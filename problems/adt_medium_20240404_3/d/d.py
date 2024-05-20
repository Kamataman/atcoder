n=int(input())
a=[]
for i in range(n):
    a.append(list(input()))

ans=[]
for i in range(n):
    ans.append(['0']*n)

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            ans[i][j]=a[i+1][j]
        elif i==0:
            ans[i][j]=a[i][j-1]
        elif i==n-1 and j==n-1:
            ans[i][j]=a[i-1][j]
        elif i==n-1:
            ans[i][j]=a[i][j+1]
        elif j==0:
            ans[i][j]=a[i+1][j]
        elif j==n-1:
            ans[i][j]=a[i-1][j]
        else:
            ans[i][j]=a[i][j]

for i in range(n):
    print(''.join(ans[i]))