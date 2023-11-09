def max_heapify(a, i, k):
    j = i
    if 2 * i + 1 < k and a[2 * i + 1] > a[j]:
        j = 2 * i + 1
    if 2 * i + 2 < k and a[2 * i + 2] > a[j]:
        j = 2 * i + 2
    if i != j:
        a[i], a[j] = a[j], a[i]
        print(a)
        max_heapify(a, j, k)


def heap_sort(a):
    n = len(a)
    for i in range(n)[::-1]:
        max_heapify(a, i, n)
    for i in range(n)[::-1]:
        a[0], a[i] = a[i], a[0]
        print(i)
        max_heapify(a, 0, i)


n = int(input())
(*a,) = map(int, input().split())
a.sort()
for i in range(n - 1):
    a[0], a[i] = a[i], a[0]
    while i > 0:
        j = (i - 1) // 2
        a[i], a[j] = a[j], a[i]
        i = j
a[0], a[-1] = a[-1], a[0]
print(*a)
