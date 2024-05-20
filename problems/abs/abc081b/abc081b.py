n=int(input())
a=list(map(int,input().split()))

flg=False
count=0
while flg==False:
    for i,ai in enumerate(a):
        if ai%2==0:
            a[i]=ai/2
        else:
            flg=True
    count+=1
count-=1
print(count)