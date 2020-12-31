MOD = 10 ** 9 + 7
n, k = map(int, input().split())
ans = 1
for i in range(n):
    ans = (ans * (k - i)) % MOD
print(ans)
