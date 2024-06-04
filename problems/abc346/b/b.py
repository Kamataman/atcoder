w,b=map(int,input().split())
PIANO='wbwbwwbwbwbw'
infPiano=''.join([PIANO]*((w+b)//len(PIANO)+2))
def contains(substr,char):
    count=0
    for s in list(substr):
        if s==char:
            count+=1
    return count

for i in range(len(PIANO)):
    substr=infPiano[i:i+w+b]
    if contains(substr,'w')==w and contains(substr,'b')==b:
        print('Yes')
        exit()
print('No')