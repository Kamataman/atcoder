n=int(input())
s=['']*n
c=['']*n
for i in range(n):
    s[i],c[i]=input().split()

c=map(int,c)
t=sum(c)
s=sorted(s)

print(s[t%n])