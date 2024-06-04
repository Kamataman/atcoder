s=input()
import itertools
h={}
for i,j in itertools.combinations(range(len(s)),2):
    l=list(s)
    tmp=l[i]
    l[i]=l[j]
    l[j]=tmp
    h[''.join(l)]=h.get(''.join(l),0)+1
print(h)