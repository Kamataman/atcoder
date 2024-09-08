n=int(input())
ans=[]
for _ in range(n):
    l,r=map(int,input().split())
    if r-l>0:
        ans.append(r)
    else:
        print('No')
        exit()
print('Yes')
print(' '.join(list(map(str,ans))))