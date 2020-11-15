import bisect


def sorted_index(A):
    # Aをソートした後のindexのリスト
    A_ = sorted(A)
    B = []
    for a in A:
        idx = bisect.bisect_left(A_, a)
        B.append(idx)
    return B


def cyclic_factorize(A):
    # Aを巡回置換分解する
    B = sorted_index(A)
    checked = [False] * len(A)
    cycle_lst = []
    for i, a in enumerate(A):
        if checked[i]:
            continue
        now = i
        checked[now] = True
        cycle = [a]
        next = B[now]
        while not checked[next]:
            now = next
            next = B[now]
            cycle.append(A[now])
            checked[now] = True
        cycle_lst.append(cycle)
    return cycle_lst


N = int(input())
(*W,) = map(int, input().split())
cycle_lst = cyclic_factorize(W)
ans = 0
global_min = min(W)
for cycle in cycle_lst:
    l = len(cycle)
    s = sum(cycle)
    local_min = min(cycle)
    ans += s + min((l - 2) * local_min, local_min + (l + 1) * global_min)
print(ans)
