n=int(input())
d=[]
for i in range(n):
    d.append(int(input()))

d.sort(reverse=True)

count=0
pre_d=101
for di in d:
    if di<pre_d:
        count+=1
    pre_d=di

print(count)