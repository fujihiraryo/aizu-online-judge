def lower_bound(a, x, key=lambda i: i):
    n = len(a)
    i, j = -1, n
    while j - i > 1:
        k = (i + j) // 2
        if x <= key(a[k]):
            j = k
        else:
            i = k
    return j


t = input()
n = len(t)
suff = list(range(n))
suff.sort(key=lambda i: t[i:])
for _ in range(int(input())):
    p = input()
    m = len(p)
    i = lower_bound(suff, p, key=lambda i: t[i:])
    if i < n and t[suff[i] : suff[i] + m] == p:
        print(1)
    else:
        print(0)
