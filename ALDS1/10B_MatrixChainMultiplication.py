from functools import lru_cache

n = int(input())
r, c = [], []
for _ in range(n):
    ri, ci = map(int, input().split())
    r.append(ri)
    c.append(ci)


@lru_cache(maxsize=10 ** 6)
def rec(i, j):
    if i + 1 == j:
        return 0
    return min(rec(i, k) + r[i] * r[k] * c[j - 1] + rec(k, j) for k in range(i + 1, j))


print(rec(0, n))
