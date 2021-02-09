n = int(input())
recs = []
x, y = [], []
for _ in range(n):
    xi, yi, xj, yj = map(int, input().split())
    recs.append((xi, yi, xj, yj))
    x.append(xi)
    x.append(xj)
    y.append(yi)
    y.append(yj)
x.sort()
y.sort()
s = [[0] * (2 * n - 1) for _ in range(2 * n - 1)]
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        s[i][j] = (x[i + 1] - x[i]) * (y[j + 1] - y[j])
xmap = {}
for i in range(2 * n):
    xmap[x[i]] = i
ymap = {}
for j in range(2 * n):
    ymap[y[j]] = j
mark = [[0] * (2 * n) for _ in range(2 * n)]
for xi, yi, xj, yj in recs:
    ix = xmap[xi]
    jx = xmap[xj]
    iy = ymap[yi]
    jy = ymap[yj]
    mark[ix][iy] += 1
    mark[ix][jy] -= 1
    mark[jx][iy] -= 1
    mark[jx][jy] += 1
for i in range(2 * n):
    for j in range(1, 2 * n):
        mark[i][j] += mark[i][j - 1]
for j in range(2 * n):
    for i in range(1, 2 * n):
        mark[i][j] += mark[i - 1][j]
ans = 0
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        if mark[i][j]:
            ans += s[i][j]
print(ans)
