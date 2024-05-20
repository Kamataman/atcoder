s=input()
n=len(s)

ans=set()
for start in range(n):
    for end in range(start,n):
        ans.add(s[start:end+1:])        
    
# print(ans)
print(len(ans))