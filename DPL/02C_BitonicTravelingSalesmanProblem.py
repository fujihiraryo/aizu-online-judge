n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
dist = [[0] * n for _ in range(n)]
for i in range(n):
    xi, yi = lst[i]
    for j in range(n):
        xj, yj = lst[j]
        dist[i][j] = ((xi - xj) ** 2 + (yi - yj) ** 2) ** (1 / 2)
dp = [[None] * n for _ in range(n)]
dp[0][1] = dist[0][1]
for j in range(1, n - 1):
    for i in range(j - 1)[::-1]:
        dp[i][j] = dp[i][j - 1] + dist[j - 1][j]
    dp[j][j + 1] = min(dp[i][j] + dist[i][j + 1] for i in range(j))
print(dp[n - 2][n - 1] + dist[n - 2][n - 1])
