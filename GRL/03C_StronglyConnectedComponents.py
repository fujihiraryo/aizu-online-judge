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


def scc(graph):
    n = len(graph)
    dfs = DFS(graph)
    order = dfs.postorder[::-1]
    index = [-1] * n
    for i, x in enumerate(order):
        index[x] = i
    reverse = [set() for _ in range(n)]
    for x in range(n):
        for y in graph[x]:
            reverse[index[y]].add(index[x])
    dfs = DFS(reverse)
    group = [-1] * n
    cnt = -1
    for i in dfs.preorder:
        if dfs.parent[i] == -1:
            cnt += 1
        group[order[i]] = cnt
    return group


n, m = map(int, input().split())
graph = [set() for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].add(y)
group = scc(graph)
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(int(group[x] == group[y]))
