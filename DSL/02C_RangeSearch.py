import bisect
import sys

lower_bound = bisect.bisect_left
upper_bound = bisect.bisect_right
input = sys.stdin.readline


class RangeSearch:
    def __init__(self, x, y):
        n = len(x)
        d = 1
        while d ** 2 < n:
            d += 1
        array = list(range(n))
        array.sort(key=lambda i: x[i])
        sorted_x = sorted(x)
        bucket = [[] for _ in range(d)]
        sorted_y = [[] for _ in range(d)]
        for i in range(n):
            bucket[i // d].append(array[i])
            sorted_y[i // d].append(y[array[i]])
        for i in range(d):
            bucket[i].sort(key=lambda i: y[i])
            sorted_y[i].sort()
        self.size = d
        self.x = x
        self.y = y
        self.sorted_x = sorted_x
        self.sorted_y = sorted_y
        self.array = array
        self.bucket = bucket

    def query(self, sx, tx, sy, ty):
        d = self.size
        ix = lower_bound(self.sorted_x, sx)
        jx = upper_bound(self.sorted_x, tx)
        if ix // d == jx // d:
            for k in self.array[ix:jx]:
                if sy <= self.y[k] <= ty:
                    yield k
            return
        for k in self.array[ix : (ix // d + 1) * d]:
            if sy <= self.y[k] <= ty:
                yield k
        for i in range(ix // d + 1, jx // d):
            iy = lower_bound(self.sorted_y[i], sy)
            jy = upper_bound(self.sorted_y[i], ty)
            for k in self.bucket[i][iy:jy]:
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
