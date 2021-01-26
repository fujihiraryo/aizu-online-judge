import sys

sys.setrecursionlimit(10 ** 7)


class DFS:
    def __init__(self, graph):
        n = len(graph)
        self.graph = graph
        self.visited = [0] * n
        self.preorder = []
        self.postorder = []
        self.parent = [-1] * n
        self.children = [[] for _ in range(n)]
        for i in range(n):
            if self.visited[i]:
                continue
            self.visit(i)

    def visit(self, x):
        self.visited[x] = 1
        self.preorder.append(x)
        for y in self.graph[x]:
            if self.visited[y]:
                continue
            self.parent[y] = x
            self.children[x].append(y)
            self.visit(y)
        self.postorder.append(x)


def bridges(graph):
    n = len(graph)
    dfs = DFS(graph)
    order = [None] * n
    for i, x in enumerate(dfs.preorder):
        order[x] = i
    lower = order[:]
    for x in dfs.preorder[::-1]:
        for y in graph[x]:
            if y == dfs.parent[x]:
                continue
            lower[x] = min(lower[x], lower[y])
    for x in range(n):
        for y in graph[x]:
            if order[x] < lower[y]:
                yield sorted((x, y))


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = sorted(list(bridges(graph)))
for x, y in ans:
    print(x, y)
