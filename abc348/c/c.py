n=int(input())
a=[0]*n
c=[0]*n
for i in range(n):
    a[i],c[i]=map(int,input().split())

ans={}
for i in range(n):
    if c[i] in ans.keys():
        if a[i]<ans[c[i]]:
            ans[c[i]]=a[i]
    else:
        ans[c[i]]=a[i]

# print(ans)
print(max(ans.values()))