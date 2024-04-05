h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

first=True

for i in range(h):
    for j in range(w):
        if s[i][j]=='o':
            if first:
                f_x=i
                f_y=j
                first=False
            else:
                dist=abs(i-f_x)+abs(j-f_y)
                print(dist)
                exit()