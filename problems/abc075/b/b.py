h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

nears=[]
for i in range(-1,1+1):
    for j in range(-1,1+1):
        nears.append([i,j])        

for i in range(h):
    for j in range(w):
        if s[i][j]!='#':
            bomb=0
            for near in nears:
                if 0 <= i + near[0] < h and 0 <= j+near[1] < w:
                    if s[i + near[0]][j+near[1]]=='#':
                        bomb+=1
            s[i][j]=str(bomb)
    print(''.join(s[i]))