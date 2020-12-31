import itertools
import bisect

n, m = map(int, input().split())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
(*c,) = map(int, input().split())
(*d,) = map(int, input().split())
ab = [a[i] + b[j] for i, j in itertools.product(range(n), repeat=2)]
cd = [c[i] + d[j] for i, j in itertools.product(range(n), repeat=2)]
cd.sort()
ans = 0
for x in ab:
    ans += bisect.bisect_right(cd, m - x) - bisect.bisect_left(cd, m - x)
print(ans)
