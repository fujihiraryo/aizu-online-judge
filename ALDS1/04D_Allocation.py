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
a, b = 0, 10 ** 10
while b - a > 1:
    c = (a + b) // 2
    if ok(c):
        b = c
    else:
        a = c
print(b)
