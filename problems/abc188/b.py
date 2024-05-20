n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

value=0
for i in range(n):
    value+=a[i]*b[i]
if value==0:
    print("Yes")
else:
    print("No")
    