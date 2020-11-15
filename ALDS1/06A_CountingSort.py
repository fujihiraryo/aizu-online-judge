def counting_sort(A):
    K = max(A) + 1
    N = len(A)
    C = [0] * K
    for a in A:
        C[a] += 1
    for k in range(1, K):
        C[k] = C[k - 1] + C[k]
    B = []
    b = 0
    for n in range(N):
        while n >= C[b]:
            b += 1
        B.append(b)
    return B


n = int(input())
(*A,) = map(int, input().split())
B = counting_sort(A)
print(*B)
