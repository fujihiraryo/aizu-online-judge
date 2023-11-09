def sub_heapify(a, i):
    n = len(a)
    j = i
    if 2 * i + 1 < n and a[2 * i + 1] > a[j]:
        j = 2 * i + 1
    if 2 * i + 2 < n and a[2 * i + 2] > a[j]:
        j = 2 * i + 2
    if i != j:
        a[i], a[j] = a[j], a[i]
        sub_heapify(a, j)


def heapify(a):
    n = len(a)
    for i in range(n)[::-1]:
        sub_heapify(a, i)


n = int(input())
(*a,) = map(int, input().split())
heapify(a)
print(" ", end="")
print(*a)
