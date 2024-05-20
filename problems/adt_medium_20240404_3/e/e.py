s=list(input())

s.reverse()

sum=0
for i,si in enumerate(s):
    ascii=ord(si)-64
    sum+=ascii*26**i

print(sum)