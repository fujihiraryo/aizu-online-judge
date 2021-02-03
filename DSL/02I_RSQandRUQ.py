import sys

input = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, n, ope=min, ide=2 ** 31 - 1):
        m = 2 ** (n - 1).bit_length()
        self.data = [0] * (2 * m)
        self.memo = [None] * (2 * m)
        self.len = [1] * (2 * m)
        for k in range(1, m)[::-1]:
            self.len[k] = self.len[2 * k] + self.len[2 * k + 1]
        self.size = m
        self.ope = ope
        self.ide = ide

    def __covering_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        i1 = (i0 // (i0 & -i0)) // 2
        j1 = (j0 // (j0 & -j0)) // 2
        while i0 < j0:
            if j0 <= j1:
                yield j0
            if i0 <= i1:
                yield i0
            i0 //= 2
            j0 //= 2
        while i0:
            yield i0
            i0 //= 2

    def __covered_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 % 2:
                yield i0
                i0 += 1
            if j0 % 2:
                j0 -= 1
                yield j0
            i0 //= 2
            j0 //= 2

    def __lazy_update(self, k):
        if self.memo[k] is None:
            return
        if k < self.size:
            self.data[2 * k] = self.memo[k] // 2
            self.memo[2 * k] = self.memo[k] // 2
            self.data[2 * k + 1] = self.memo[k] // 2
            self.memo[2 * k + 1] = self.memo[k] // 2
        self.memo[k] = None

    def range_update(self, i, j, x):
        covering = [*self.__covering_index(i, j)]
        for k in covering[::-1]:
            self.__lazy_update(k)
        for k in self.__covered_index(i, j):
            print(i, j, k)
        #     self.memo[k] = x * self.len[k]
        #     self.data[k] = x * self.len[k]
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 % 2:
                self.memo[i0] = x
                self.data[i0] = x
                i0 += 1
            if j0 % 2:
                j0 -= 1
                self.memo[j0] = x
                self.data[j0] = x
            i0 //= 2
            j0 //= 2
            x *= 2
        for k in covering:
            left = self.data[2 * k]
            right = self.data[2 * k + 1]
            self.data[k] = self.ope(left, right)

    def range_ope(self, i, j):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = self.ope(x, self.data[k])
        return x


n, q = map(int, input().split())
a = LazySegmentTree(n, ope=lambda x, y: x + y, ide=0)
for _ in range(q):
    cmd, *query = map(int, input().split())
    if cmd == 0:
        s, t, x = query
        a.range_update(s, t + 1, x)
    else:
        s, t = query
        print(a.range_ope(s, t + 1))
