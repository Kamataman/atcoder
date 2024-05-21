n=int(input())
a=list(map(int,input().split()))

i=1
while i<len(a):
    if abs(a[i-1]-a[i])!=1:
        if a[i-1]<a[i]:
            insertList=[_ for _ in range(a[i-1]+1,a[i])]
            a[i:i]=insertList
            i+=len(insertList)
        else:
            insertList=[_ for _ in range(a[i-1]-1,a[i],-1)]
            a[i:i]=insertList
            i+=len(insertList)
    i+=1

print(' '.join(map(str,a)))