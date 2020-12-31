MOD = 10 ** 9 + 7
n, k = map(int, input().split())
if n < k:
    print(0)
    exit()
fct, ict = [1] * n, [1] * n
for i in range(1, n):
    fct[i] = fct[i - 1] * i % MOD
    ict[i] = ict[i - 1] * pow(i, MOD - 2, MOD) % MOD
print(fct[n - 1] * ict[k - 1] * ict[n - k] % MOD)
