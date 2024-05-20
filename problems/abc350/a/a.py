s=input()

num=int(s[3:])
if num==316:
    print('No')
    exit()
for i in range(1,350):
    if i==num:
        print('Yes')
        exit()
print('No')