s=input()

i=0
for c in s:
    if i%2==0:
        if c.isupper():
            print('No')
            exit()
    else:
        if c.islower():
            print('No')
            exit()
    i+=1
print('Yes')