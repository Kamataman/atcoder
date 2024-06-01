n,l,r=map(int,input().split())
ans=[]
for i in range(1,l):
    ans.append(i)
for i in reversed(range(l,r+1)):
    ans.append(i)
for i in range(r+1,n+1):
    ans.append(i)
print(' '.join(list(map(str,ans))))