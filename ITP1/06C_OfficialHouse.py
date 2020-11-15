n = int(input())
H = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    H[b - 1][f - 1][r - 1] += v
for b in range(4):
    for f in range(3):
        A = map(str, H[b][f])
        a = " " + " ".join(A)
        print(a)
    if b == 3:
        exit()
    print("#" * 20)
