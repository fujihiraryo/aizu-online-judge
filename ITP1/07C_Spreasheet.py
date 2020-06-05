r, c = map(int, input().split())
A = []
for i in range(r):
    *Ai, = map(int, input().split())
    Ai.append(sum(Ai))
    A.append(Ai)
B = [sum([A[i][j] for i in range(r)]) for j in range(c + 1)]
for a in A:
    print(*a)
print(*B)
