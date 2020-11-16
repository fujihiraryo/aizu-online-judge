n = int(input())
A = map(lambda x: int(x) - 1, input().split())
B = [None] * n
for i, x in enumerate(map(lambda x: int(x) - 1, input().split())):
    B[x] = i
C = []


def step(i, j):
    if i >= j:
        return
    a = next(A)
    k = B[a]
    step(i, k)
    step(k + 1, j)
    C.append(a)


step(0, n)
print(*map(lambda x: x + 1, C))
