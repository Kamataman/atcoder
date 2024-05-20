n=int(input())
s=input()
q=int(input())

ope={}

for i in range(q):
    c,d=input().split()
    
    if ope.get(c)==None:
        ope[c]=d

    for item in ope.items():
        if item[1]==c:
            ope[item[0]]=d

# print(ope)

s_list=list(s)
for i,char in enumerate(s_list):
    if ope.get(char):
        s_list[i]=ope[char]

print("".join(s_list))



