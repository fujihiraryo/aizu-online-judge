def factrize(x):
    # 試し割りによるxの素因数分解
    f = {}
    tmp = x
    i = 2
    while i ** 2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp = tmp // i
        if cnt > 0:
            f[i] = cnt
        i += 1
    if tmp != 1 or f == {}:
        f[tmp] = 1
    return f


n = int(input())
f = factrize(n)
ans = 1
for p in f:
    ans *= p ** (f[p] - 1) * (p - 1)
print(ans)
