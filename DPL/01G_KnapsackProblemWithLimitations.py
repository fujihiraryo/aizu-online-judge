def split(x):
    t = 1
    y = 0
    while y + t < x:
        yield t
        y += t
        t *= 2
    yield x - y


def main():
    n, m = map(int, input().split())
    v, w, c = [], [], []
    for _ in range(n):
        vi, wi, ci = map(int, input().split())
        v.append(vi)
        w.append(wi)
        c.append(ci)
    _v, _w = [], []
    for i in range(n):
        for k in split(c[i]):
            _v.append(v[i] * k)
            _w.append(w[i] * k)
    v, w = _v, _w
    n = len(v)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        wi, vi = w[i - 1], v[i - 1]
        for j in range(wi, m + 1)[::-1]:
            dp[j] = max(dp[j], dp[j - wi] + vi)
    print(dp[m])


main()
