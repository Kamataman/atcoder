h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(map(str,input())))
#print(s)

angle=0
for i in range(1,h-1):
    for j in range(1,w-1):
        count=0
        if s[i][j]=='#':
            if s[i-1][j-1]=='#':count+=1 
            if s[i-1][j]=='#':count+=1 
            if s[i-1][j+1]=='#':count+=1 
            if s[i][j+1]=='#':count+=1 
            if s[i+1][j+1]=='#':count+=1 
            if s[i+1][j]=='#':count+=1 
            if s[i+1][j-1]=='#':count+=1 
            if s[i][j-1]=='#':count+=1 
        if count==3:
            angle+=1
print(angle)