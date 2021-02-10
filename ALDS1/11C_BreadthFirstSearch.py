def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = [start]
    for x in queue:
        for y in graph[x]:
            if dist[y] != -1:
                continue
            queue.append(y)
            dist[y] = dist[x] + 1
    return dist


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    x, _, *lst = map(int, input().split())
    for y in lst:
        graph[x - 1].append(y - 1)
dist = bfs(graph, 0)
for x in range(n):
    print(x + 1, dist[x])
