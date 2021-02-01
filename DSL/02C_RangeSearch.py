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


class RangeSearch:
    def __init__(self, x, y):
        key_x = lambda i: x[i]
        key_y = lambda i: y[i]
        n = len(x)
        d = 1
        while d ** 2 < n:
            d += 1
        array = list(range(n))
        array.sort(key=key_x)
        bucket = [[] for _ in range(d)]
        for i in range(n):
            bucket[i // d].append(array[i])
        for i in range(d):
            bucket[i].sort(key=key_y)
        self.size = d
        self.x = x
        self.y = y
        self.key_x = key_x
        self.key_y = key_y
        self.array = array
        self.bucket = bucket

    def query(self, sx, tx, sy, ty):
        d = self.size
        ix = lower_bound(self.array, sx, key=self.key_x)
        jx = upper_bound(self.array, tx, key=self.key_x)
        if ix // d == jx // d:
            for k in self.array[ix:jx]:
                if sy <= self.y[k] <= ty:
                    yield k
            return
        for k in self.array[ix : (ix // d + 1) * d]:
            if sy <= self.y[k] <= ty:
                yield k
        for bucket in self.bucket[ix // d + 1 : jx // d]:
            iy = lower_bound(bucket, sy, key=self.key_y)
            jy = upper_bound(bucket, ty, key=self.key_y)
            for k in bucket[iy:jy]:
                yield k
        for k in self.array[(jx // d) * d : jx]:
            if sy <= self.y[k] <= ty:
                yield k


def main():
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


main()
