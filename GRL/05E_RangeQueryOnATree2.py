class BIT:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * (n + 1)

    def __getitem__(self, i):
        return self.sum(i + 1) - self.sum(i)

    def sum(self, i):
        s = 0
        tmp = i
        while tmp:
            s += self.arr[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        tmp = i + 1
        while tmp <= self.size:
            self.arr[tmp] += x
            tmp += tmp & -tmp


class RangeBIT:
    def __init__(self, n):
        self.bit0 = BIT(n)
        self.bit1 = BIT(n)

    def add(self, i, j, x):
        self.bit0.add(i, -x * i)
        self.bit0.add(j, x * j)
        self.bit1.add(i, x)
        self.bit1.add(j, -x)

    def sum(self, i, j):
        si = self.bit0.sum(i) + self.bit1.sum(i) * i
        sj = self.bit0.sum(j) + self.bit1.sum(j) * j
        return sj - si


class HLD:
    def __init__(self, tree, root=0):
        n = len(tree)
        parent = [root] * n
        children = [[] for _ in range(n)]
        order = []
        queue = [root]
        for x in queue:
            order.append(x)
            for y in tree[x]:
                if y == parent[x]:
                    continue
                parent[y] = x
                children[x].append(y)
                queue.append(y)
        size = [1] * n
        for x in order[::-1]:
            for y in children[x]:
                size[x] += size[y]
        group = [-1] * n
        index = [-1] * n
        time = 0
        for x in order:
            if index[x] != -1:
                continue
            leader = x
            while True:
                group[x] = leader
                index[x] = time
                time += 1
                if size[x] == 1:
                    break
                x = max(children[x], key=lambda i: size[i])
        self.parent = parent
        self.group = group
        self.index = index
        self.bit = RangeBIT(n)

    def add(self, x, w):
        y = x
        while y != self.parent[y]:
            g = self.group[y]
            j = self.index[y]
            i = max(1, self.index[g])
            self.bit.add(i, j + 1, w)
            y = self.parent[g]

    def sum(self, x):
        s = 0
        y = x
        while y != self.parent[y]:
            g = self.group[y]
            j = self.index[y]
            i = self.index[g]
            s += self.bit.sum(i, j + 1)
            y = self.parent[g]
        return s


n = int(input())
tree = [[] for _ in range(n)]
for x in range(n):
    (*raw,) = map(int, input().split())
    if raw[0] == 0:
        continue
    for y in raw[1:]:
        tree[x].append(y)
        tree[y].append(x)
hld = HLD(tree)
for _ in range(int(input())):
    query = tuple(map(int, input().split()))
    if query[0] == 0:
        _, x, w = query
        hld.add(x, w)
    else:
        _, x = query
        print(hld.sum(x))
