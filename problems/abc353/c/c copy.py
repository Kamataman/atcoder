n=int(input())
a=list(map(int,input().split()))

sum=0
for i in range(n):
    sum+=a[i]*(n-1)

a.sort()

right=n-1
count=0
for i in range(n):
    while right-i>=1:
        if a[i]+a[right]>=10**8:
            count+=1
            right-=1
        else:
            break
    right=n-1
print(sum-count*10**8)