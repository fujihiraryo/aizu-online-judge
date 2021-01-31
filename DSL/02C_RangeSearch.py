def lower_bound(a, x, key=lambda i: i):
    n = len(a)
    i, j = -1, n
    while j - i > 1:
        k = (i + j) // 2
        if x <= key(a[k]):
            j = k
        else:
            i = k
    return j


def upper_bound(a, x, key=lambda i: i):
    n = len(a)
    i, j = -1, n
    while j - i > 1:
        k = (i + j) // 2
        if x < key(a[k]):
            j = k
        else:
            i = k
    return j


def merge(a, b, key=lambda i: i):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c + a[i:] + b[j:]


class RangeSearch:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        n = len(x)
        self.size = 1 << n.bit_length()
        self.tree = [[] for _ in range(self.size << 1)]
        idx = list(range(n))
        idx.sort(key=lambda i: x[i])
        self.idx = idx
        for i in range(n):
            self.tree[i + self.size] = [idx[i]]
        for i in range(1, self.size)[::-1]:
            left = self.tree[2 * i]
            right = self.tree[2 * i + 1]
            self.tree[i] = merge(left, right, key=lambda i: y[i])

    def query(self, sx, tx, sy, ty):
        ix = lower_bound(self.idx, sx, key=lambda i: self.x[i])
        jx = upper_bound(self.idx, tx, key=lambda i: self.x[i])
        ix += self.size
        jx += self.size
        while ix < jx:
            if ix & 1:
                iy = lower_bound(self.tree[ix], sy, key=lambda i: y[i])
                jy = upper_bound(self.tree[ix], ty, key=lambda i: y[i])
                for k in range(iy, jy):
                    yield self.tree[ix][k]
                ix += 1
            if jx & 1:
                iy = lower_bound(self.tree[jx - 1], sy, key=lambda i: y[i])
                jy = upper_bound(self.tree[jx - 1], ty, key=lambda i: y[i])
                for k in range(iy, jy):
                    yield self.tree[jx - 1][k]
            ix >>= 1
            jx >>= 1


n = int(input())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
rs = RangeSearch(x, y)
q = int(input())
for _ in range(q):
    sx, tx, sy, ty = map(int, input().split())
    for i in sorted(rs.query(sx, tx, sy, ty)):
        print(i)
    print()
