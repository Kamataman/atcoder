import math
l=int(input())

def conbinatin(a,b):
    return math.factorial(a)//(math.factorial(b)*math.factorial(a-b))

print(conbinatin(l-1,11))