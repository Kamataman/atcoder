n,k=map(int,input().split())
s=[]
for i in range(n):
    s.append(input())

s=s[:k]
s.sort()
for i in range(k):
    print(s[i])
