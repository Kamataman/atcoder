a,b,c,d=map(int,input().split())

def calc(c,d):
    c_=c//4
    d_=d//2
    s=c_*d_/2
    cmod=c%4
    if cmod==1:
        s+=d_*3/2
    elif cmod==2:
        s+=d_*3
    elif cmod==3:
        s+=d_*7/2
    
    dmod=d%2
    if dmod==1:
        if cmod==0:
            s+=c_*2   
        elif cmod==1:
            s+=c_*2+1            
        elif cmod==2:
            s+=c_*2+3/2            
        elif cmod==3:
            s+=c_*2+3/2            
    return s*2    

s=calc(c-a,d-b)
print(s)