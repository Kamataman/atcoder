a,b,c,d=map(lambda x: x+10**9,map(int,input().split()))

def calc(x,y):
    s1=(x//4)*(y//2)*8
    s2_pattern=[0,3,6,7]
    s2=s2_pattern[x%4]*(y//2)
    s3_pattern=[0,4]
    s3=s3_pattern[y%2]*(x//4)
    s4_pattern=[[0,0,0,0],[0,2,3,3]]
    s4=s4_pattern[y%2][x%4]
    # print(s1,s2,s3,s4)
    return s1+s2+s3+s4

ans=calc(c,d)-calc(a,d)-calc(c,b)+calc(a,b)
print(ans)