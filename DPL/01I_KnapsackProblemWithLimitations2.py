N, W = map(int, input().split())
itemsA, itemsB = [], []
for _ in range(N):
    v, w, m = map(int, input().split())
    itemsA.append((v, w, min(m, 50)))
    itemsB.append((v, w, m - min(m, 50)))

# itemsAを1+2+4+8...の形に分解する
itemsA_decomposed = []
for v, w, m in itemsA:
    k = 1
    while m > 0:
        if m >= k:
            itemsA_decomposed.append((v * k, w * k))
            m -= k
        else:
            itemsA_decomposed.append((v * m, w * m))
            break
        k *= 2

# itemsA_decomposedの先頭N個を使って価値Vを得る最小の重さDP[N][V]を求める
L = len(itemsA_decomposed)
DP = [[10**20] * (50 * 50 * 50 + 1) for _ in range(L + 1)]
DP[0][0] = 0
for i in range(L):
    v, w = itemsA_decomposed[i]
    for j in range(50 * 50 * 50 + 1):
        if j < v:
            DP[i + 1][j] = DP[i][j]
        else:
            DP[i + 1][j] = min(DP[i][j], DP[i][j - v] + w)

# 各Vに対して、DP[-1][V]<=Wならば残りのW-DP[-1][V]をitemsBから貪欲に埋める
itemsB.sort(key=lambda item: item[0] / item[1], reverse=True)
ans = 0
for V in range(50 * 50 * 50 + 1):
    v_sum = V
    w_sum = DP[-1][V]
    if w_sum > W:
        continue
    for v, w, m in itemsB:
        cnt = min((W - w_sum) // w, m)
        v_sum += cnt * v
        w_sum += cnt * w
    ans = max(ans, v_sum)
print(ans)
