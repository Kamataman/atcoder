n=int(input())
a=[0]*n
c=[0]*n
min_cost={}
for i in range(n):
    a[i],c[i]=map(int,input().split())
    min_cost[a[i]-1]=c[i]
    min_cost[a[i]]=c[i]

now_cost=10**9
for key in sorted(min_cost.keys(),reverse=True):
    now_cost=min(min_cost[key],now_cost)
    min_cost[key]=now_cost

cards=[]
for i in range(n):
    if c[i]==min_cost[a[i]-1]:
        cards.append(i+1)

print(len(cards))
print(' '.join(map(str,cards)))