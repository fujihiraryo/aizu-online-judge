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
    for x in step(i, B[a]):
        yield x
    for x in step(B[a] + 1, j):
        yield x
    yield a


print(*map(lambda x: x + 1, step(0, n)))
