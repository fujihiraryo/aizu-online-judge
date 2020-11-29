import heapq

INF = 10 ** 20
n, m, r = map(int, input().split())
G = [{} for i in range(n)]
for j in range(m):
    s, t, d = map(int, input().split())
    G[s][t] = d
INF = 10 ** 20
D = [INF for i in range(n)]
D[r] = 0
Q = [(0, r)]
heapq.heapify(Q)
while Q:
    _, x = heapq.heappop(Q)
    for y in G[x].keys():
        if D[x] + G[x][y] < D[y]:
            D[y] = D[x] + G[x][y]
            heapq.heappush(Q, (D[y], y))
for i in range(n):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])
