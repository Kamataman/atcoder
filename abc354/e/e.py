import itertools
import copy

n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())

dp=[False]*2**n 
dp[0]=False 
for i in range(1,2**n): #小さいほうから確定していく
    for comb in itertools.combinations(range(n),2): #nから2つ選ぶ組み合わせをすべて試行する
        if i >> comb[0] & 1 and i>>comb[1] & 1: #組み合わせについてビットが立っていたら（カードが残っていたら）
            if (a[comb[0]]==a[comb[1]] or b[comb[0]]==b[comb[1]]) and not dp[i^(1<<comb[0])^(1<<comb[1])]: #表裏どちらかが数字が同じでそれを取り除いたらdpがfalseだったら
                dp[i]=True

print('Takahashi') if dp[(1<<n)-1] else print('Aoki')