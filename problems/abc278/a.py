n,k=map(int,input().split())
a=input().split()

for i in range(k):
    a.pop(0)
    a.append('0')

print(' '.join(a))