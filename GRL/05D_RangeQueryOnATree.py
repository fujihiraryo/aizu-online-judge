import sys

sys.setrecursionlimit(10 ** 7)


class DFS:
    def __init__(self, graph):
        n = len(graph)
        self.graph = graph
        self.visited = [0] * n
        self.preorder = []
        self.postorder = []
        self.pretime = [0] * n
        self.posttime = [0] * n
        self.time = 0
        self.parent = [-1] * n
        self.children = [[] for _ in range(n)]
        for i in range(n):
            if self.visited[i]:
                continue
            self.visit(i)

    def visit(self, x):
        self.visited[x] = 1
        self.preorder.append(x)
        self.pretime[x] = self.time
        self.time += 1
        for y in self.graph[x]:
            if self.visited[y]:
                continue
            self.parent[y] = x
            self.children[x].append(y)
            self.visit(y)
        self.postorder.append(x)
        self.posttime[x] = self.time
        self.time += 1


class FenwickTree:
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


# construct
n = int(input())
graph = [[] for _ in range(n)]
for x in range(n):
    (*raw,) = map(int, input().split())
    if raw[0] == 0:
        continue
    for y in raw[1:]:
        graph[x].append(y)
        graph[y].append(x)
dfs = DFS(graph)
ft = FenwickTree(2 * n)
# query
q = int(input())
query_list = [tuple(map(int, input().split())) for _ in range(q)]
for query in query_list:
    if query[0] == 0:
        _, x, w = query
        i, j = dfs.pretime[x], dfs.posttime[x]
        ft.add(i, w)
        ft.add(j, -w)
    else:
        _, x = query
        i = dfs.posttime[x]
        print(ft.sum(i))
