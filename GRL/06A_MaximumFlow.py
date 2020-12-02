INF = 1 << 30
n, m = map(int, input().split())
adj_matrix = [[0] * n for _ in range(n)]
adj_list = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj_matrix[a][b] = c
    adj_list[a].append(b)
    adj_list[b].append(a)
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
        for y in adj_list[x]:
            if visited[y] or adj_matrix[x][y] == 0:
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
        min_capacity = min(min_capacity, adj_matrix[x][y])
        y = x
    # update graph
    y = goal
    while parent[y] is not None:
        x = parent[y]
        adj_matrix[x][y] -= min_capacity
        adj_matrix[y][x] += min_capacity
        y = x
    max_flow += min_capacity
print(max_flow)
