n=int(input())
a=list(map(int,input().split()))

UPPER=2*10**5+1
memo=[0]*UPPER

a.sort()
for ai in a:
    memo[ai]+=1
count=0
for i in range(UPPER):
    count+=memo[i]
    memo[i]=count

sum=0
for ai in a:
    sum+=memo[ai-1]*(len(a)-memo[ai])

# print(a)
# print(memo[:10])
print(sum)