n,a,b=map(int,input().split())

ans_sum=0    
for i in range(1,n+1):
    # keta_sum=i//10**4+i//10**3+i//10**2+i//10**1+i%10**1
    keta_sum=sum(map(int,str(i)))
    if a<=keta_sum and keta_sum<=b:
        ans_sum+=i

print(ans_sum)