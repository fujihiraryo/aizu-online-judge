import heapq

INF = 1 << 30


def dijkstra(graph, start):
    dist = [INF] * len(graph)
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    while heap:
        _, x = heapq.heappop(heap)
        for y in graph[x]:
            if dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
                heapq.heappush(heap, (dist[y], y))
    return dist


n = int(input())
graph = [{} for _ in range(n)]
for _ in range(n - 1):
    x, y, w = map(int, input().split())
    graph[x][y] = w
    graph[y][x] = w
dist_from_0 = dijkstra(graph, 0)
x = max(range(n), key=lambda x: dist_from_0[x])
dist_from_x = dijkstra(graph, x)
y = max(range(n), key=lambda x: dist_from_x[x])
dist_from_y = dijkstra(graph, y)
for i in range(n):
    print(max(dist_from_x[i], dist_from_y[i]))
