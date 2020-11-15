n, m = map(int, input().split())
(*C,) = map(int, input().split())
# n, m = 15, 6
# C = [1, 2, 7, 8, 12, 50]
# DP[i][j]=i種類以内でj円払う最小枚数
inf = 10 ** 10
DP = [[inf for j in range(n + 1)] for i in range(m + 1)]
DP[0][0] = 0
for i in range(m):
    for j in range(n + 1):
        if j < C[i]:
            DP[i + 1][j] = DP[i][j]
        else:
            DP[i + 1][j] = min(DP[i][j], DP[i + 1][j - C[i]] + 1)
print(DP[m][n])
