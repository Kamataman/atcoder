n=int(input())
count=0
l=len(range(-n+1,n+1))
print(l)
for i in range(-n+1,n+1):
    s=(l*(2*i+l-1))/2
    l-=2
    if s==n:
        count+=1
    print('i %d  s %d' %(i,s))

print(count)