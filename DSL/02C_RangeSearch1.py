import bisect
import heapq

lower_bound = bisect.bisect_left
upper_bound = bisect.bisect_right


class RangeSearch:
    def __init__(self, x, y):
        n = len(x)
        self.x = x
        self.y = y
        self.size = 1 << n.bit_length()
        self.tree = [[] for _ in range(self.size << 1)]
        self.sorted_y = [[] for _ in range(self.size << 1)]
        idx = list(range(n))
        idx.sort(key=lambda i: x[i])
        self.sorted_x = sorted(x)
        self.idx = idx
        for i in range(n):
            self.tree[i + self.size].append(idx[i])
            self.sorted_y[i + self.size].append(self.y[idx[i]])
        for i in range(1, self.size)[::-1]:
            left = zip(self.sorted_y[2 * i], self.tree[2 * i])
            right = zip(self.sorted_y[2 * i + 1], self.tree[2 * i + 1])
            merged = list(heapq.merge(left, right))
            self.sorted_y[i] = [yk for yk, k in merged]
            self.tree[i] = [k for yk, k in merged]
        # exit()

    def query(self, sx, tx, sy, ty):
        ix = lower_bound(self.sorted_x, sx)
        jx = upper_bound(self.sorted_x, tx)
        ix += self.size
        jx += self.size
        while ix < jx:
            if ix & 1:
                iy = lower_bound(self.sorted_y[ix], sy)
                jy = upper_bound(self.sorted_y[ix], ty)
                for k in range(iy, jy):
                    yield self.tree[ix][k]
                ix += 1
            if jx & 1:
                iy = lower_bound(self.sorted_y[jx - 1], sy)
                jy = upper_bound(self.sorted_y[jx - 1], ty)
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
    for k in sorted(rs.query(sx, tx, sy, ty)):
        print(k)
    print()
