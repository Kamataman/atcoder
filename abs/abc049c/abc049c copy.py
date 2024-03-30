DREAM='dream'
DREAMER='dreamer'
ERASE='erase'
ERASER='eraser'

def check_func(s):
    ret_list=[]
    if s.startswith(DREAM):
        ret_list.append(s[len(DREAM)::])
    if s.startswith(DREAMER):
        ret_list.append(s[len(DREAMER)::])
    if s.startswith(ERASE):
        ret_list.append(s[len(ERASE)::])
    if s.startswith(ERASER):
        ret_list.append(s[len(ERASER)::])

    if len(ret_list)==0:
        return 'NO'
    elif '' in ret_list:
        return 'YES'
    else:
        for substr in ret_list:
            if check_func(substr)=='YES':
                return 'YES'
        return 'NO'
    
s=input()
print(check_func(s))
