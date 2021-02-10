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
for _ in range(n):
    x, _, *lst = map(int, input().split())
    for y, c in zip(lst[0::2], lst[1::2]):
        graph[x][y] = c
dist = dijkstra(graph, 0)
for x in range(n):
    print(x, dist[x])
