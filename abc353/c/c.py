n=int(input())
a=list(map(int,input().split()))

l=[0]*10**8
for ai in a:
    l[ai-1]+=1
for i in range(1,10**8):
    l[i]+=l[i-1]

sum=0
count=0
for ai in a:
    sum+=ai*(n-1)
    count+=n-l[(10**8-ai)-1]
    
print(sum-count*10**8)