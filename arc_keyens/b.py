n,k=map(int,input().split())
ball=list(map(int,input().split()))

ballcount=[0]*(max(ball)+1)
for i,value in enumerate(ball):
    ballcount[value]+=1

answer=0
deathboxindex=k
boxes=[-1]*k
for ballnumber,count in enumerate(ballcount):
    for i in range(deathboxindex):
        if count>=i+1:
            boxes[i]+=1
        else:
            answer+=boxes[i]+1
            deathboxindex=count
            
for i in range(deathboxindex):
    answer+=boxes[i]+1
print(answer)
        