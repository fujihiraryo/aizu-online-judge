inf = 10 ** 9 + 7


def merge(A, left, mid, right):
    cnt = 0
    L = A[left:mid]
    R = A[mid:right]
    L.append(inf)
    R.append(inf)
    i, j = 0, 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        cnt += 1
    return cnt


def merge_sort(A, left, right):
    cnt = 0
    if left + 1 < right:
        mid = (left + right) // 2
        cnt += merge_sort(A, left, mid)
        cnt += merge_sort(A, mid, right)
        cnt += merge(A, left, mid, right)
    return cnt


n = int(input())
(*A,) = map(int, input().split())
cnt = merge_sort(A, 0, n)
print(*A)
print(cnt)
