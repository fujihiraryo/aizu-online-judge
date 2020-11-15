n, m, p = map(int, input().split())
A = []
for i in range(n):
    (*Ai,) = map(int, input().split())
    A.append(Ai)
B = []
for i in range(m):
    (*Bi,) = map(int, input().split())
    B.append(Bi)
for i in range(n):
    Ci = [sum([A[i][j] * B[j][k] for j in range(m)]) for k in range(p)]
    print(*Ci)
