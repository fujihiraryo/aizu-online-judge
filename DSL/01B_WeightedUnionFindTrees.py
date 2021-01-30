class WeightedUnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [0] * n

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
            self.parent[i] = j
            self.weight[i] += self.weight[j]
        return j

    def diff(self, i, j):
        if self.find(i) != self.find(j):
            return None
        return self.weight[j] - self.weight[i]

    def unite(self, i, j, w):
        i0, j0 = self.find(i), self.find(j)
        w0 = w + self.weight[i] - self.weight[j]
        if i0 == j0:
            return
        if i0 > j0:
            i0, j0 = j0, i0
            w0 = -w0
        self.parent[j0] = i0
        self.weight[j0] = w0


n, q = map(int, input().split())
wuf = WeightedUnionFind(n)
for _ in range(q):
    (*query,) = map(int, input().split())
    if query[0] == 0:
        x, y, w = query[1:]
        wuf.unite(x, y, w)
    else:
        x, y = query[1:]
        ans = wuf.diff(x, y)
        if ans is None:
            print("?")
        else:
            print(ans)
