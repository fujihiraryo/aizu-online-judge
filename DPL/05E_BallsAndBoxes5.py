MOD = 10 ** 9 + 7
n, k = map(int, input().split())
if n > k:
    print(0)
    exit()
fct, ict = [1] * (k + 1), [1] * (k + 1)
for i in range(1, k + 1):
    fct[i] = fct[i - 1] * i % MOD
    ict[i] = ict[i - 1] * pow(i, MOD - 2, MOD) % MOD
print(fct[k] * ict[n] * ict[k - n] % MOD)
