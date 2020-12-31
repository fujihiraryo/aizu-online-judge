MOD = 10 ** 9 + 7
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][1] = 1
    for j in range(2, k + 1):
        dp[i][j] = dp[i][j - 1]
        if i >= j:
            dp[i][j] += dp[i - j][j]
            dp[i][j] %= MOD
print(dp[n][k])
