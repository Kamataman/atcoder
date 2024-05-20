n=int(input())
p_list=list(map(int,input().split()))

#set=[() for i in range(2**n)]
retSet=set([0])
for p in p_list:
    tmpSet=set([])
    for s in retSet:
        tmpSet.add(s+p)
    retSet=retSet | tmpSet

print(len(retSet))