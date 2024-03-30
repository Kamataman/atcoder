h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

h-=1
w-=1

def pos_nw(x,y):
    if x-1<0 or y-1<0:
        return None
    else:
        return s[y-1][x-1]
def pos_n(x,y):
    if y-1<0:
        return None
    else:
        return s[y-1][x]
def pos_ne(x,y):
    if x+1>w or y-1<0:
        return None
    else:
        return s[y-1][x+1]
def pos_e(x,y):
    if x+1>w:
        return None
    else:
        return s[y][x+1]
def pos_se(x,y):
    if x+1>w or y+1>h:
        return None
    else:
        return s[y+1][x+1]
def pos_s(x,y):
    if y+1>h:
        return None
    else:
        return s[y+1][x]
def pos_sw(x,y):
    if x-1<0 or y+1>h:
        return None
    else:
        return s[y+1][x-1]
def pos_w(x,y):
    if x-1<0:
        return None
    else:
        return s[y][x-1]

for i in range(h+1):
    for j in range(w+1):
        if s[i][j]!='#':
            bomb=0
            if pos_nw(j,i)=='#':
                bomb+=1
            if pos_n(j,i)=='#':
                bomb+=1
            if pos_ne(j,i)=='#':
                bomb+=1
            if pos_e(j,i)=='#':
                bomb+=1
            if pos_se(j,i)=='#':
                bomb+=1
            if pos_s(j,i)=='#':
                bomb+=1
            if pos_sw(j,i)=='#':
                bomb+=1
            if pos_w(j,i)=='#':
                bomb+=1
            s[i][j]=str(bomb)
    print(''.join(s[i]))