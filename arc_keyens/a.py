N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[0]*N
a_max=a[0]
c[0]=a[0]*b[0]
for i in range(1,N):
    a_max=max(a_max,a[i])
    c[i]=max(c[i-1],a_max*b[i])
print('\n'.join(map(str,c)))