INF = 10**20
n = int(input()) + 1
(*p,) = map(float, input().split())
(*q,) = map(float, input().split())
p = [0] + p
# s[i] = sum(p[0:i]) + sum(q[0:i])
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + p[i - 1] + q[i - 1]


def sm(i, j):
    # [i:j]で探索が終わる確率
    return s[j] - s[i] - p[i]


# dp[i][j] = [i:j]で作る最小コスト
dp = [[INF] * (n + 1) for i in range(n)]


def rec(i, j):
    if i + 1 == j:
        dp[i][j] = q[i]
    elif dp[i][j] == INF:
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], rec(i, k) + rec(k, j) + sm(i, j))
    return dp[i][j]


print(rec(0, n))
