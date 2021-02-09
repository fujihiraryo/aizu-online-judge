n = int(input())
lim = 1001
mark = [[0] * lim for _ in range(lim)]
for i in range(n):
    xi, yi, xj, yj = map(int, input().split())
    mark[xi][yi] += 1
    mark[xj][yj] += 1
    mark[xi][yj] -= 1
    mark[xj][yi] -= 1
for i in range(lim):
    for j in range(1, lim):
        mark[i][j] += mark[i][j - 1]
for j in range(lim):
    for i in range(1, lim):
        mark[i][j] += mark[i - 1][j]
ans = 0
for i in range(lim):
    for j in range(lim):
        ans = max(ans, mark[i][j])
print(ans)
