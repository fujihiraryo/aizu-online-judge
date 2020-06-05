while True:
    n = int(input())
    if n == 0:
        exit()
    *a, = map(int, input().split())
    m = sum(a) / len(a)
    s = (sum([(m - ai)**2 for ai in a]) / len(a))**0.5
    print(s)
