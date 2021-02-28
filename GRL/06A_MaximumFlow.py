def max_flow(graph, start, goal, INF=1 << 30):
    n = len(graph)
    flow = 0
    while True:
        # bfs
        dist = [INF] * n
        dist[start] = 0
        queue = [start]
        for x in queue:
            for y in graph[x]:
                if graph[x][y] == 0 or dist[y] < INF:
                    continue
                dist[y] = dist[x] + 1
                queue.append(y)
        if dist[goal] == INF:
            break
        # dfs
        checked = [[0] * n for _ in range(n)]
        f = INF
        while f:
            f = dfs(graph, dist, checked, start, goal, INF)
            flow += f
    return flow


def dfs(graph, dist, checked, x, goal, flow):
    if x == goal:
        return flow
    for y in graph[x]:
        if graph[x][y] == 0 or dist[x] >= dist[y] or checked[x][y]:
            continue
        checked[x][y] = 1
        f = dfs(graph, dist, checked, y, goal, min(flow, graph[x][y]))
        if f:
            graph[x][y] -= f
            graph[y][x] += f
            return f
    return 0


n, m = map(int, input().split())
graph = [{} for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = 0
print(max_flow(graph, 0, n - 1))
