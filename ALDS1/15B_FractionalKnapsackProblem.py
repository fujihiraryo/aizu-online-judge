n, w = map(int, input().split())
lst = []
for _ in range(n):
    v, u = map(int, input().split())
    lst.append((v / u, v, u))
lst.sort(reverse=True)
weight = 0
value = 0
for _, v, u in lst:
    if weight + u < w:
        weight += u
        value += v
    else:
        value += v * (w - weight) / u
        break
print(value)
