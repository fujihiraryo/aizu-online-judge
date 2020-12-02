INF = 1 << 30
n, m = map(int, input().split())
graph = [{} for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = 0
start, goal = 0, n - 1
max_flow = 0
while True:
    # find path
    visited = [0] * n
    stack = [start]
    parent = [None] * n
    while stack:
        x = stack.pop()
        visited[x] = 1
        if x == goal:
            break
        for y in graph[x].keys():
            if visited[y] or graph[x][y] == 0:
                continue
            stack.append(y)
            parent[y] = x
    if x != goal:
        break
    # min capacity
    y = goal
    min_capacity = INF
    while parent[y] is not None:
        x = parent[y]
        min_capacity = min(min_capacity, graph[x][y])
        y = x
    # update graph
    y = goal
    while parent[y] is not None:
        x = parent[y]
        graph[x][y] -= min_capacity
        graph[y][x] += min_capacity
        y = x
    max_flow += min_capacity
print(max_flow)
