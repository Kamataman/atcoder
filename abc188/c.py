n=int(input())
rate=list(map(int,input().split()))
player=[i for i in range(2**n)]

while len(player)!=2:
    winners=[]
    for i in [i*2+1 for i in range(int(len(player)/2))]:
        if rate[player[i-1]]<rate[player[i]]:
            winners.append(player[i])
        else:
            winners.append(player[i-1])
    player=winners

if rate[player[0]] < rate[player[1]]:
    print(player[0]+1)
else:
    print(player[1]+1) 
