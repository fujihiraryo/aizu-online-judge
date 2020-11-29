class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parents = [i for i in range(n)]

    def find(self, i):
        tmp = i
        while self.parents[tmp] != tmp:
            tmp = self.parents[tmp]
        return tmp

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parents[j0] = i0


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
uf = UnionFind(n)
ans = 0
for i, j, w in edges:
    if uf.find(i) != uf.find(j):
        uf.unite(i, j)
        ans += w
print(ans)
