n,d,p=map(int,input().split())
f=list(map(int,input().split()))

f.sort(reverse=True)
i=0
fee=0
while i<n:
    win_sum=sum(f[i:i+d if i+d<n else n])
    if win_sum>p:
        fee+=p
    else:
        fee+=win_sum
    i=i+d if i+d<n else n
print(fee)