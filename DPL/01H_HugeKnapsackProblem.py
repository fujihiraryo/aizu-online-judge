import bisect

n, m = map(int, input().split())
v, w = [], []
for _ in range(n):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)
# 前半の全列挙
n0 = n // 2
v0, w0 = [0], [0]
cnt = 1
for i in range(n0):
    for j in range(cnt):
        v0.append(v[i] + v0[j])
        w0.append(w[i] + w0[j])
        cnt += 1
idx = sorted(range(1 << n0), key=lambda i: w0[i])
v0 = [v0[i] for i in idx]
w0 = [w0[i] for i in idx]
tmp = 0
for i in range(1 << n0):
    if tmp > v0[i]:
        v0[i] = tmp
    tmp = max(tmp, v0[i])
# 後半の全列挙
n1 = n - n0
v1, w1 = [0], [0]
cnt = 1
for i in range(n1):
    for j in range(cnt):
        v1.append(v[i + n0] + v1[j])
        w1.append(w[i + n0] + w1[j])
        cnt += 1
# 二分探索
ans = 0
for i in range(1 << n1):
    if w1[i] <= m:
        j = max(0, bisect.bisect_right(w0, m - w1[i]) - 1)
        ans = max(ans, v0[j] + v1[i])
print(ans)
