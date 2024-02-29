def nextdate(h,m):
    if m < 59:
        return h,m+1
    else:
        if h < 23:
            return h+1,0
        else:
            return 0,0

def changedate(h,m):
    a,b=divmod(h,10)
    c,d=divmod(m,10)
    return a*10+c,b*10+d

def isMimachigaiDate(h,m):
    hd,md=changedate(h,m)
    return True if 0<=hd and hd<24 and 0<=md and md<60 else False

h,m=map(int,input().split())

while not(isMimachigaiDate(h,m)):
    h,m=nextdate(h,m)

print(h,m)