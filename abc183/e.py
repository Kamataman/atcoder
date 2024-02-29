h, w = map(int, input().split())
s = []

for i in range(h):
    s.append(list(input()))

dp = [[0]*w for p in range(h)]
dp[0][1] = 1
dp[1][0] = 1

for i in range(h):
    for j in range(w):
        for ii in range(i):
            dp[i][j] += dp[ii][j]
        for jj in range(j):
            dp[i][j] += dp[i][jj]
        for ii in range(i):
            for jj in range(j):
                if ii == jj:
                    dp[i][j] += dp[ii][jj]
        if s[i][j] == '#':
            dp[i][j] = 0
            print(dp[i][j])
print(dp)
