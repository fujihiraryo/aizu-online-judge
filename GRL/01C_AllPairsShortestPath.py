INF = 10 ** 18
n, m = map(int, input().split())
G = [[INF] * n for i in range(n)]
for _ in range(m):
    i, j, d = map(int, input().split())
    G[i][j] = d
for i in range(n):
    G[i][i] = 0
    for j in range(n):
        G[i][j] = G[i][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])
if any(G[i][i] < 0 for i in range(n)):
    print("NEGATIVE CYCLE")
    exit()
for i in range(n):
    for j in range(n):
        if G[i][j] > INF // 10:
            G[i][j] = "INF"
for i in range(n):
    print(*G[i])
