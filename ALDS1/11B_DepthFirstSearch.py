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


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    x, _, *lst = map(int, input().split())
    for y in lst:
        graph[x - 1].append(y - 1)
dfs = DFS(graph)
for x in range(n):
    print(x + 1, dfs.pretime[x] + 1, dfs.posttime[x] + 1)
