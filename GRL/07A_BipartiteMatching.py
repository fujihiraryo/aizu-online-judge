def maximum_flow(graph, start, goal):
    INF = 1 << 30
    n = len(graph)
    max_flow = 0
    while True:
        # find path
        visited = [0] * n
        stack = [start]
        last = [None] * n
        while stack:
            x = stack.pop()
            visited[x] = 1
            if x == goal:
                break
            for y in graph[x].keys():
                if visited[y] or graph[x][y] == 0:
                    continue
                stack.append(y)
                last[y] = x
        if x != goal:
            break
        # min capacity
        y = goal
        min_capacity = INF
        while last[y] is not None:
            x = last[y]
            min_capacity = min(min_capacity, graph[x][y])
            y = x
        # update graph
        y = goal
        while last[y] is not None:
            x = last[y]
            graph[x][y] -= min_capacity
            graph[y][x] += min_capacity
            y = x
        max_flow += min_capacity
    return max_flow


a, b, m = map(int, input().split())
n = a + b + 2
graph = [{} for _ in range(n)]
for i in range(1, a + 1):
    graph[0][i] = 1
    graph[i][0] = 0
for i in range(a + 1, a + b + 1):
    graph[i][n - 1] = 1
    graph[n - 1][i] = 0
for _ in range(m):
    x, y = map(int, input().split())
    graph[x + 1][y + a + 1] = 1
    graph[y + a + 1][x + 1] = 0
print(maximum_flow(graph, 0, n - 1))
