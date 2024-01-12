from collections import deque


def slide_max(a, k):
    n = len(a)
    d = deque()
    b = []
    i = 0
    while len(b) < n:
        if i < n:
            while d and a[d[-1]] <= a[i]:
                d.pop()
            d.append(i)
        if i >= k - 1:
            b.append(a[d[0]])
        if d and d[0] <= i + 1 - k:
            d.popleft()
        i += 1
    return b


n, m = map(int, input().split())
v, w, c = [], [], []
for _ in range(n):
    vi, wi, ci = map(int, input().split())
    v.append(vi)
    w.append(wi)
    c.append(ci)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    table = [[] for _ in range(w[i - 1])]
    for j in range(m + 1)[::-1]:
        r = (m - j) % w[i - 1]
        x = (m - j) // w[i - 1]
        table[r].append(dp[i - 1][j] + x * v[i - 1])
    sm = [slide_max(table[r], c[i - 1] + 1) for r in range(w[i - 1])]
    for j in range(m + 1):
        r = (m - j) % w[i - 1]
        x = (m - j) // w[i - 1]
        dp[i][j] = sm[r][x] - x * v[i - 1]
print(dp[n][m])
