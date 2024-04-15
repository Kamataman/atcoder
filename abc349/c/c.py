s=input()
t=input()

t=t.lower()
now_t=0
for si in s:
    if  si==t[now_t]:
        now_t+=1
        if now_t==2:
            if t[now_t]=='x':
                print('Yes')
                exit()
        if now_t==3:
            print('Yes')
            exit()
            
print('No')