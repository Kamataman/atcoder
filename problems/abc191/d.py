import math
x,y,r=map(float,input().split())

def adfloor(n):
    return math.floor(n) if n>0 else -math.floor(abs(n))

count=0
for i in range(adfloor(y-r),adfloor(y+r)+1):
    xans=math.sqrt(r*r-(i-y)*(i-y))
    
    if xans==0:
        count+=1
    elif (x+xans).is_integer():
        count+=math.floor(2*xans)+1
    elif (x-xans).is_integer():
        count+=math.floor(2*xans)+1
    else:
        count+=math.floor(2*xans)
    '''
    for j in range(adfloor(x-r),adfloor(x+r)+1):
        if x-xans<=j and j<=x+xans:
            count+=1
    '''
print(count)