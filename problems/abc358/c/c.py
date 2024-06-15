n,m=map(int,input().split())
s=[input() for _ in range(n)]

for i in range(n):
    mod_s=[]
    for moji in list(s[i]):
        if moji=='o':
            mod_s.append(True)
        else:
            mod_s.append(False)
    s[i]=mod_s

ans=10
# すべての組み合わせ
for i in range(1,1<<n+1):
    aji=[False]*m
    # すべてのお店
    for j in range(n):
        if i & (1<<j):
            # すべての味
            for k in range(m):
                aji[k]=s[j][k] or aji[k]
    if not (False in aji):
        ans=min(ans,i.bit_count())

print(ans)