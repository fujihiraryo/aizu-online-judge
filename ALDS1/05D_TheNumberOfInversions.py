inf = 10 ** 9 + 7


def merged(L, R):
    cnt = 0
    l, r = len(L), len(R)
    L.append(inf)
    R.append(inf)
    lst = []
    i, j = 0, 0
    for k in range(l + r):
        if L[i] < R[j]:
            lst.append(L[i])
            i += 1
        else:
            lst.append(R[j])
            j += 1
            # まだ追加されていないLの要素数
            cnt += l - i
    return lst, cnt


def merge_sorted(A):
    lenA = len(A)
    if lenA == 1:
        return A, 0
    half = lenA // 2
    L, cntL = merge_sorted(A[:half])
    R, cntR = merge_sorted(A[half:])
    A, cnt = merged(L, R)
    return A, cntL + cntR + cnt


n = int(input())
(*A,) = map(int, input().split())
A, cnt = merge_sorted(A)
print(cnt)
