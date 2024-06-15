s=input()
upper=0
lower=0
for si in s:
    if si.isupper():
        upper+=1
    else:
        lower+=1
if upper>lower:
    s=s.upper()
else:
    s=s.lower()
print(s)