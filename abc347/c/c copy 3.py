n,a,b=map(int,input().split())
d=list(map(int,input().split()))

events=set()
for di in d:
    events.add(di%(a+b))

max=-1
min=a+b
for event in events:
    if event <min:
        min=event
    if max<event:
        max=event
if max-min<a+b-max+min:
    need_cont_holiday=max-min+1
else:
    need_cont_holiday=a+b-max+min+1

print(max)
print(min)
print(need_cont_holiday)
if need_cont_holiday<=a:
    print('Yes')
else:
    print('No')
