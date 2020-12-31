from collections import defaultdict

INF = 10 ** 7
n, m = map(int, input().split())
graph = [defaultdict(lambda: INF) for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a][b] = d
dp = [[INF] * (1 << n) for _ in range(n)]
dp[0][0] = 0
for s in range(1 << n):
    for i in range(n):
        if (1 << i) & s:
            dp[i][s] = min(dp[j][s - (1 << i)] + graph[j][i] for j in range(n))
ans = dp[0][(1 << n) - 1]
print(ans if ans < INF else -1)
