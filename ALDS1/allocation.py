def ok(P):
    # 積載量PのトラックK台以内で運べるかどうか
    cnt = 0
    truck = 0
    for w in W + [0]:
        if w > P:
            return False
        if truck + w <= P:
            truck += w
        else:
            truck = w
            cnt += 1
    if cnt + 1 <= K:
        return True
    else:
        return False


N, K = map(int, input().split())
W = [int(input()) for _ in range(N)]
l, r = 0, 10**10
while r - l > 1:
    c = (l + r) // 2
    if ok(c):
        r = c
    else:
        l = c
print(r)
