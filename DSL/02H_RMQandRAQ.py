class RMQandRAQ:
    def __init__(self, n):
        d = 1
        while d ** 2 <= n:
            d += 1
        self.size = d
        self.bucket = [[0] * d for _ in range(d)]
        self.bucket_min = [0] * d
        self.add_memo = [0] * d
        self.min = lambda lst: min(lst, default=1 << 30)

    def lazy_add(self, i):
        d = self.size
        for j in range(d):
            self.bucket[i][j] += self.add_memo[i]
        self.add_memo[i] = 0

    def range_add(self, k0, k1, x):
        d = self.size
        i0, j0 = k0 // d, k0 % d
        i1, j1 = k1 // d, k1 % d
        self.lazy_add(i0)
        self.lazy_add(i1)
        if i0 == i1:
            for j in range(j0, j1):
                self.bucket[i0][j] += x
            self.bucket_min[i0] = min(self.bucket[i0])
            return
        for j in range(j0, d):
            self.bucket[i0][j] += x
        self.bucket_min[i0] = min(self.bucket[i0])
        for i in range(i0 + 1, i1):
            self.add_memo[i] += x
            self.bucket_min[i] += x
        for j in range(j1):
            self.bucket[i1][j] += x
        self.bucket_min[i1] = min(self.bucket[i1])

    def range_min(self, k0, k1):
        d = self.size
        i0, j0 = k0 // d, k0 % d
        i1, j1 = k1 // d, k1 % d
        self.lazy_add(i0)
        self.lazy_add(i1)
        if i0 == i1:
            return min(self.bucket[i0][j0:j1])
        return min(
            self.min(self.bucket_min[i0 + 1 : i1]),
            self.min(self.bucket[i0][j0:d]),
            self.min(self.bucket[i1][0:j1]),
        )


n, q = map(int, input().split())
a = RMQandRAQ(n)
for _ in range(q):
    (*query,) = map(int, input().split())
    if query[0] == 0:
        i, j, x = query[1:]
        a.range_add(i, j + 1, x)
    else:
        i, j = query[1:]
        print(a.range_min(i, j + 1))
