S = input()
T = input()
# S = "acac"
# T = "acm"
# DP[i][j]=Sのi文字とTのj文字の編集距離
m, n = len(S), len(T)
DP = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(m + 1):
    DP[i][0] = i
for j in range(n + 1):
    DP[0][j] = j
for i in range(1, m + 1):
    for j in range(1, n + 1):
        c = DP[i - 1][j - 1] + int(S[i - 1] != T[j - 1])
        DP[i][j] = min(DP[i - 1][j] + 1, DP[i][j - 1] + 1, c)
print(DP[m][n])
