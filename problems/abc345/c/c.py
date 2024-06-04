s=input()
letters=[0]*(ord('z')-ord('a')+1)
for l in s:
    letters[ord(l)-ord('a')]+=1
n=len(s)
ans=n*(n-1)//2
nochange=False
for l in letters:
    if l>1:
        ans-=l*(l-1)//2
        nochange=True
if nochange:
    ans+=1
print(ans)