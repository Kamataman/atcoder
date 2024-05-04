s=list(input())
t=list(input())

now=0
ans=[]
for i,ti in enumerate(t):
    if ti==s[now]: 
        ans.append(str(i+1))
        now+=1
print(' '.join(ans))

        

