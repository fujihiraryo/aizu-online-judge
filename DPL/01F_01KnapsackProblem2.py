n, m = map(int, input().split())
VW = [tuple(map(int, input().split())) for i in range(n)]
V = [v for v, w in VW]
W = [w for v, w in VW]
# n, m = 4, 5
# V = [4, 5, 2, 8]
# W = [2, 2, 1, 3]
# DP[i][j]=i個の品物で価値j以上で最小の重さ
sv = sum(V)
inf = 10 ** 10
DP = [[inf for j in range(sv + 1)] for i in range(n + 1)]
DP[0][0] = 0
for i in range(n):
    for j in range(sv + 1):
        if j < V[i]:
            DP[i + 1][j] = DP[i][j]
        else:
            DP[i + 1][j] = min(DP[i][j], DP[i][j - V[i]] + W[i])
for j in range(sv, 0, -1):
    if DP[n][j] <= m:
        print(j)
        exit()
print(0)
