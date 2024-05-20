n=int(input())
s=[]
for i in range(n):
    s.append(str(input()))

def rec(i):
    if i==0:
        if s[i]=='AND':
            return 1
        if s[i]=='OR':
            return 3
    else:
        if s[i]=='AND':
            return rec(i-1)
        if s[i]=='OR':
            return 2**(i+1)+rec(i-1)

print(rec(n-1))