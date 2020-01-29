N = int(input())
A = [int(input()) for n in range(N)]
B, C = [], []
m = 10 ** 9
M = 0
for n in range(N):
    if A[n] < m:
        m = A[n]
    if A[N - n - 1] > M:
        M = A[N - n - 1]
    B.append(m)
    C.append(M)
C.reverse()
D = [C[n+1] - B[n] for n in range(N-1)]
print(max(D))
