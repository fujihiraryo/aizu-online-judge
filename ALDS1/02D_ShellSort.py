import copy


def insertion_sort(A_, n, g, cnt):
    A = copy.copy(A_)
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v
    return A, cnt


def shell_sort(A_, n):
    A = copy.copy(A_)
    cnt = 0
    G = [(3 ** i - 1) // 2 for i in range(13, 0, -1) if (3 ** i - 1) // 2 <= n]
    m = len(G)
    for i in range(m):
        A, cnt = insertion_sort(A, n, G[i], cnt)
    return m, G, cnt, A


n = int(input())
A = [int(input()) for i in range(n)]
m, G, cnt, A = shell_sort(A, n)

print(m)
print(*G)
print(cnt)
for a in A:
    print(a)
