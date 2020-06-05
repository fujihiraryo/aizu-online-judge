def factrize(x):
    # 試し割りによるxの素因数分解
    f = {}
    tmp = x
    i = 2
    while i**2 <= tmp:
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


n = map(int, input().split())
*A, = map(int, input().split())
A = [factrize(a) for a in A]
F = {}
for f in A:
    for p in f:
        try:
            F[p] = max(F[p], f[p])
        except KeyError:
            F[p] = f[p]
ans = 1
for p in F:
    ans *= p**F[p]
print(ans)
