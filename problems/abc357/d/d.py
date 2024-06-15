n=input()
keta=len(n)
n=int(n)
v=0
for i in range(n):
    v+=n*10**(keta*i)
print(v)