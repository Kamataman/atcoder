import copy
n=int(input())
a=list(map(int,input().split()))

p=[]
l={}
for i in range(n-1,0,-1):
    keta=len(str(a[i]))
    l[keta]=l.get(keta,0)+1
    p.append(copy.deepcopy(l.copy()))
p.reverse()
# print(p)
sum=0
for i in range(n):
    if i!=n-1:
        for keta in p[i].keys():
            sum+=a[i]*10**keta*p[i][keta]
            # print(keta,p[i][keta],sum)
    sum+=a[i]*i
    # print(sum)
    
print(sum%998244353)