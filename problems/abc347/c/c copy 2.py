n,a,b=map(int,input().split())
d=list(map(int,input().split()))

week=['h']*a+['w']*b
# print(week)

events=set()
for di in d:
    events.add(di%(a+b))
    

for startday in range(a+b):
    d_check=True
    for event in events:
        # print('{} {}'.format(startday,event))
        checkday=(startday+event)%(a+b)
        if week[checkday]=='w':
            d_check=False
            break
    
    if d_check:
        print('Yes')
        exit()

print('No')