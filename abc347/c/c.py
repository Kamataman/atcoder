n,a,b=map(int,input().split())
d=list(map(int,input().split()))

events=set()
for di in d:
    events.add(di%(a+b))

events=list(events)
events.sort()

pre_event=events[0]
max=-1
min=a+b
max_dist=0
for event in events:
    if event <min:
        min=event
    if max<event:
        max=event
    if event-pre_event>max_dist:
        max_dist=event-pre_event
    pre_event=event
if max-min<a+b-max_dist:
    need_cont_holiday=max-min+1
else:
    need_cont_holiday=a+b-max_dist+1
    
if need_cont_holiday<=a:
    print('Yes')
else:
    print('No')
