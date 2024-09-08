s=input()
t=input()
l=len(s)

x=[]

s_mod=list(s)

while "".join(s_mod)!=t:
    cand=[]
    for i in range(l):
        if s_mod[i]!=t[i]:
            temp=list(s_mod)
            temp[i]=t[i]
            cand.append("".join(temp))
    if cand:
        s_mod=sorted(cand)[0]
        x.append(s_mod)

print(len(x))
[print(_) for _ in x]