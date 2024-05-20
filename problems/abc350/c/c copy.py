n=int(input())
a=list(map(int,input().split()))

steps=[]

for j in range(0,n-1):
    for i in range(n-1,j,-1):
        if a[i-1]>a[i]:
            steps.append([i,i+1])
            a[i-1],a[i]=a[i],a[i-1]

# print(a)
print(len(steps))
for step in steps:
    print(' '.join(map(str,step)))