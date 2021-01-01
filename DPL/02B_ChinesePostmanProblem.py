from collections import defaultdict


def generate_matching(lst):
    if len(lst) == 0:
        yield []
        return
    x = lst[0]
    for i in range(1, len(lst)):
        y = lst[i]
        for matching in generate_matching([z for z in lst if z != x and z != y]):
            yield [(x, y)] + matching


INF = 1 << 30
n, m = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(m)]
# 隣接リスト構築
graph = [defaultdict(lambda: INF) for _ in range(n)]
for x, y, d in edge:
    graph[x][y] = min(graph[x][y], d)
    graph[y][x] = min(graph[y][x], d)
# ワーシャルフロイド
dist = [[INF] * n for _ in range(n)]
for x in range(n):
    dist[x][x] = 0
    for y in graph[x]:
        dist[x][y] = graph[x][y]
for z in range(n):
    for x in range(n):
        for y in range(n):
            dist[x][y] = min(dist[x][y], dist[x][z] + dist[z][y])
# 次数が奇数の点を列挙
deg = [0] * n
for x, y, d in edge:
    deg[x] += 1
    deg[y] += 1
odd_lst = [x for x in range(n) if deg[x] % 2]
# 最小マッチング
min_cost = INF
for matching in generate_matching(odd_lst):
    min_cost = min(min_cost, sum(dist[x][y] for x, y in matching))
print(min_cost + sum(d for x, y, d in edge))
