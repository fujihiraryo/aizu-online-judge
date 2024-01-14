from collections import deque


def slmax(a, k):
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
v, w, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    v[i], w[i], c[i] = map(int, input().split())
dp = [0] * (m + 1)
for i in range(n):
    for j in range(w[i]):
        q = (m - j) // w[i]
        lst = []
        for k in range(q + 1)[::-1]:
            lst.append(dp[j + k * w[i]] - k * v[i])
        sm = slmax(lst, c[i] + 1)[::-1]
        for k in range(q + 1):
            dp[j + k * w[i]] = sm[k] + k * v[i]
print(dp[m])
