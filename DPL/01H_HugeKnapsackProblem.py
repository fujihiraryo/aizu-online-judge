import bisect

INF = 10 ** 20
n, m = map(int, input().split())
v, w = [], []
for _ in range(n):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)
n0 = n // 2
wv0 = []
for s in range(1 << n0):
    vi, wi = 0, 0
    for i in range(n0):
        if (1 << i) & s:
            vi += v[i]
            wi += w[i]
    wv0.append([wi, vi])
wv0.sort()
tmp = 0
for i in range(1 << n0):
    if tmp > wv0[i][1]:
        wv0[i][1] = tmp
    tmp = max(tmp, wv0[i][1])
n1 = n - n0
wv1 = []
for s in range(1 << n1):
    vi, wi = 0, 0
    for i in range(n1):
        if (1 << i) & s:
            vi += v[i + n0]
            wi += w[i + n0]
    wv1.append([wi, vi])
ans = 0
for x in wv1:
    if x[0] <= m:
        i = max(0, bisect.bisect_right(wv0, [m - x[0], INF]) - 1)
        ans = max(ans, x[1] + wv0[i][1])
print(ans)
print(wv0)
print(wv1)
