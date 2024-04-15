s=input()
# s=''.join(['a' for _ in range(100)])
# print(s)
counts=[0]*26
for si in s:
    counts[ord(si)-ord('a')]+=1

# print(counts)
for i in range(1,101):
    c=0
    for count in counts:
        if count==i:
            c+=1
    if not (c==0 or c==2):
        print('No')
        exit()

print('Yes')