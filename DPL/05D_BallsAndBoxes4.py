MOD = 10 ** 9 + 7
n, k = map(int, input().split())
fct, ict = [1] * (n + k), [1] * (n + k)
for i in range(1, n + k):
    fct[i] = fct[i - 1] * i % MOD
    ict[i] = ict[i - 1] * pow(i, MOD - 2, MOD) % MOD
print(fct[n + k - 1] * ict[n] * ict[k - 1] % MOD)
