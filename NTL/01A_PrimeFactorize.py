n = int(input())
F = {}
tmp = n
i = 2
while i ** 2 <= tmp:
    cnt = 0
    while tmp % i == 0:
        cnt += 1
        tmp //= i
    if cnt > 0:
        F[i] = cnt
    i += 1
if tmp != 1 or F == {}:
    F[tmp] = 1
G = []
for p in F:
    for i in range(F[p]):
        G.append(str(p))
G = " ".join(G)
print(f"{n}: {G}")
