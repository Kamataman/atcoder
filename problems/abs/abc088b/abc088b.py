n=input()
a=list(map(int,input().split()))

a.sort(reverse=True)

score_a=0
score_b=0
for i,ai in enumerate(a):
    if i%2==0:
        score_a+=ai
    else:
        score_b+=ai

print(score_a-score_b)
