h, w = map(int, input().split())
c = [input().split() for _ in range(h)]
dp = [[0] * w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == "1":
            continue
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        ans = max(ans, dp[i][j])
print(ans ** 2)
