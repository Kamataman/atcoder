DREAM='dream'[::-1]
DREAMER='dreamer'[::-1]
ERASE='erase'[::-1]
ERASER='eraser'[::-1]
    
s=input()

i=0
s=s[::-1]
while s!='':    
    if s.startswith(DREAM):
        s=s[len(DREAM)::]
    elif s.startswith(DREAMER):
        s=s[len(DREAMER)::]
    elif s.startswith(ERASE):
        s=s[len(ERASE)::]
    elif s.startswith(ERASER):
        s=s[len(ERASER)::]
    else:
        print('NO')
        exit()
print('YES')