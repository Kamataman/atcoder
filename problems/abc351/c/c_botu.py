N=int(input())
a=list(map(int,input().split()))

count=0
temp=0
tempstart=a[0]
beforeEqual=False
for i in range(1,N):
    diff=a[i]-a[i-1]
    if diff>=2:
        count+=temp+1
        temp=0
        tempstart=-1
    elif diff==1:
        temp+=1
        if tempstart==-1:
            tempstart=a[i-1]
    elif diff==0:
        count+=1
        temp=0
        tempstart+=1
        beforeEqual=True
    elif diff<0:
        if beforeEqual:
            if tempstart==a[i]:
                tempstart+=1
        else:
            count+=temp+1
            temp=0
            tempstart=-1
            
# count+=temp+1
    
print(count)