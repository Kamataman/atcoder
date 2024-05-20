s=input()

chars=list(s)

def func():
    for i,char in enumerate(chars):
        if i==2:
            if chars[0]==chars[1]:
                if chars[0]==chars[2]:
                    # aaa
                    longchar=chars[0]
                else:
                    # aab
                    return 3
            else:
                if chars[0]==chars[2]:
                    # aba
                    return 2
                else:
                    # abb
                    return 1

        elif i>2:
            if char!=longchar:
                return i+1
            
print(func())