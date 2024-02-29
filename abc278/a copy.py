n,k=map(int,input().split())
a=input().split()

if n>k:
    retList=a[k:n]
    [retList.append('0') for i in range(n-k+1)] 

else:
    retList=[]
    [retList.append('0') for i in range(n)] 

print(' '.join(retList))