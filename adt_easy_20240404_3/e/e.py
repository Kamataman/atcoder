s=list(input())

def transInt(chr):
    return ord(chr)-64

sum=0
s.reverse()

for i,si in enumerate(s):
    sum+=transInt(si)*26**i

print(sum)
