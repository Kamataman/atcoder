n,m,t=map(int,input().split())
time=0
battery=n
for i in range(m):
    a,b=map(int,input().split())
    if battery-(a-time)<=0:
        print('No')
        exit()
    if battery+b-a-(a-time)>=n:
        battery=n
    else:
        battery=battery+b-a-(a-time)
    time=b
    #print(battery)
if battery-(t-time)<=0:
    print('No')
else:
    print('Yes')
