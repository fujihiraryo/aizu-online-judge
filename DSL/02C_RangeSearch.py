import bisect

lower_bound = bisect.bisect_left
upper_bound = bisect.bisect_right


class RangeSearch:
    def __init__(self, x, y):
        n = len(x)
        d = 1
        while d ** 2 < n:
            d += 1
        idx = sorted(range(n), key=lambda i: x[i])
        bucket = [[] for _ in range(d)]
        for i, k in enumerate(idx):
            bucket[i // d].append(k)
        for i in range(d):
            bucket[i].sort(key=lambda i: y[i])
        self.size = d
        self.bucket = bucket
        self.x = x
        self.y = y
        self.sorted_x = [x[k] for k in idx]
        self.sorted_y = [[y[k] for k in bucket[i]] for i in range(d)]

    def query(self, sx, tx, sy, ty):
        d = self.size
        ix = lower_bound(self.sorted_x[d - 1 :: d], sx)
        jx = upper_bound(self.sorted_x[0::d], tx)
        for i in range(ix, jx):
            iy = lower_bound(self.sorted_y[i], sy)
            jy = upper_bound(self.sorted_y[i], ty)
            for k in self.bucket[i][iy:jy]:
                if sx <= self.x[k] <= tx and sy <= self.y[k] <= ty:
                    yield k


n = int(input())
x, y = zip(*[map(int, input().split()) for _ in range(n)])
rs = RangeSearch(x, y)
q = int(input())
for _ in range(q):
    sx, tx, sy, ty = map(int, input().split())
    for k in sorted(rs.query(sx, tx, sy, ty)):
        print(k)
    print()
