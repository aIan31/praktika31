import sys
M = 10**9+7
n = int(sys.stdin.buffer.read())
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    for j in range(n, i-1, -1):
        dp[j] += dp[j-i]
        if dp[j] >= M:
            dp[j] -= M
print(dp[n])