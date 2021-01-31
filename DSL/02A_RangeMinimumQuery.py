class RMQ:
    def __init__(self, n, INF=2 ** 31 - 1):
        d = 1
        while d ** 2 <= n:
            d += 1
        self.size = d
        self.bucket = [[INF] * d for _ in range(d)]
        self.bucket_min = [INF] * d
        self.min = lambda x: min(x, default=INF)

    def update(self, k, x):
        d = self.size
        i, j = k // d, k % d
        self.bucket[i][j] = x
        self.bucket_min[i] = min(self.bucket[i])

    def range(self, k0, k1):
        d = self.size
        i0, j0 = k0 // d, k0 % d
        i1, j1 = k1 // d, k1 % d
        if i0 == i1:
            return min(self.bucket[i0][j0:j1])
        return min(
            self.min(self.bucket_min[i0 + 1 : i1]),
            self.min(self.bucket[i0][j0:d]),
            self.min(self.bucket[i1][0:j1]),
        )


n, q = map(int, input().split())
srd = RMQ(n)
for _ in range(q):
    (*query,) = map(int, input().split())
    if query[0] == 0:
        i, x = query[1], query[2]
        srd.update(i, x)
    else:
        i, j = query[1], query[2]
        print(srd.range(i, j + 1))
