def partition(A, a, b):
    x = A[b - 1]
    i = a - 1
    for j in range(a, b - 1):
        if A[j][1] <= x[1]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[b - 1] = A[b - 1], A[i + 1]
    return i + 1


def quick_sort(A, a, b):
    if b - a > 1:
        q = partition(A, a, b)
        quick_sort(A, a, q)
        quick_sort(A, q, b)


n = int(input())
A = []
for i in range(n):
    a, b = input().split()
    A.append((a, int(b)))
dct0 = {}
for a in A:
    dct0[a[1]] = []
for a in A:
    dct0[a[1]].append(a[0])
quick_sort(A, 0, n)
dct1 = {}
for a in A:
    dct1[a[1]] = []
for a in A:
    dct1[a[1]].append(a[0])
if dct0 == dct1:
    print("Stable")
else:
    print("Not stable")
for a in A:
    print(*a)
