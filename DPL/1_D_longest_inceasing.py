import bisect
n = int(input())
A = [int(input()) for i in range(n)]
# n = 5
# A = [5, 1, 3, 2, 4]
L = [A[0]]
for i in range(n):
    if A[i] > L[-1]:
        L.append(A[i])
    else:
        j = bisect.bisect_left(L, A[i])
        L[j] = A[i]
print(len(L))
