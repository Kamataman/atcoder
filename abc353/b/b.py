n,k=map(int,input().split())
a=list(map(int,input().split()))

start_count=0
now_riders=0
for ai in a:
    if k-now_riders>=ai:
        now_riders+=ai
    else:
        start_count+=1
        now_riders=ai
start_count+=1
print(start_count)