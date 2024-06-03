n,m,k=map(int,input().split())
c,a,r=[],[],[]
for i in range(m):
    line=input().split()
    c.append(int(line[0]))
    a.append(list(map(int,line[1:c[i]+1])))
    r.append(line[-1])

ans=0
for cand in range(1<<n):
    ok=True
    for i in range(m):
        # テストと同じビットが立っている個数を調べる
        cnt=0
        for ai in a[i]:
            cnt+=(cand>>(ai-1))&1
        # (cnt>=k) ：A  (r[i]=='o') :B
        #       B
        #     | T  | F 
        # A T | OK | NG
        #   F | NG | OK
        ok&=(cnt>=k)==(r[i]=='o')
    ans+=ok #Trueなら1足される
print(ans)