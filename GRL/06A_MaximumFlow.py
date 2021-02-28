class Dinic:
    def __init__(self, graph, start, goal, INF=1 << 30):
        n = len(graph)
        self.size = n
        self.graph = graph
        self.start = start
        self.goal = goal
        self.INF = INF

    def bfs(self):
        self.dist = [self.INF] * self.size
        self.dist[self.start] = 0
        queue = [self.start]
        for x in queue:
            for y in self.graph[x]:
                if self.graph[x][y] == 0 or self.dist[y] < self.INF:
                    continue
                self.dist[y] = self.dist[x] + 1
                queue.append(y)

    def dfs(self, x, flow):
        if x == self.goal:
            return flow
        for y in self.graph[x]:
            capa = self.graph[x][y]
            if capa == 0 or self.dist[x] >= self.dist[y] or self.checked[x][y]:
                continue
            self.checked[x][y] = 1
            f = self.dfs(y, min(flow, capa))
            if f:
                self.graph[x][y] -= f
                self.graph[y][x] += f
                return f
        return 0

    def max_flow(self):
        res = 0
        while True:
            self.bfs()
            if self.dist[self.goal] == self.INF:
                return res
            flow = self.INF
            self.checked = [[0] * self.size for _ in range(self.size)]
            while flow:
                flow = self.dfs(self.start, self.INF)
                res += flow


n, m = map(int, input().split())
graph = [{} for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = 0
print(Dinic(graph, 0, n - 1).max_flow())
