n, m = map(int, input().split())
VW = [tuple(map(int, input().split())) for i in range(n)]
V = [v for v, w in VW]
W = [w for v, w in VW]
# n, m = 4, 5
# V = [4, 5, 2, 8]
# W = [2, 2, 1, 3]
# DP[i][j]=i個の品物で重さj以内で最大価値
DP = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(n):
    for j in range(m + 1):
        if j < W[i]:
            DP[i + 1][j] = DP[i][j]
        else:
            DP[i + 1][j] = max(DP[i][j], DP[i][j - W[i]] + V[i])
print(DP[n][m])
