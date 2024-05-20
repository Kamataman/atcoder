import sympy
l,r=map(int,input().split())

devided=[]
while True:
    if l==0:
        fact2=60
        next=2**fact2
        while next>r:
            fact2-=1
            next=2**fact2
    else:
        factors: dict=sympy.factorint(l)
        fact2=factors.pop(2) if 2 in factors else 0
        next=2**fact2*(l//(2**fact2)+1)
        while next>r:
            fact2-=1
            next=2**fact2*(l//(2**fact2)+1)
        
    devided.append([l,next])
    l=next
    if next==r:
        break

print(len(devided))
for dev in devided:
    print(' '.join(list(map(str,dev))))