import bisect

n, k, x, y = map(int, input().split())
(*a,) = map(int, input().split())
# 前半の全列挙
n0 = n // 2
s0 = [0]
for i in range(n0):
    for j in range(len(s0)):
        s0.append(a[i] + s0[j])
t0 = [[] for _ in range(n0 + 1)]
for i in range(1 << n0):
    t0[bin(i).count("1")].append(s0[i])
for i in range(n0):
    t0[i].sort()
# 後半の全列挙
n1 = n - n0
s1 = [0]
for i in range(n1):
    for j in range(len(s1)):
        s1.append(a[i + n0] + s1[j])
t1 = [[] for _ in range(n1 + 1)]
for i in range(1 << n1):
    t1[bin(i).count("1")].append(s1[i])
# 二分探索
ans = 0
for i in range(n1 + 1):
    if i + n0 < k or k < i:
        continue
    for j in range(len(t1[i])):
        right = bisect.bisect_right(t0[k - i], y - t1[i][j])
        left = bisect.bisect_left(t0[k - i], x - t1[i][j])
        ans += right - left
print(ans)
