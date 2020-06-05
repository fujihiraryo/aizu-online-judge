while True:
    x, y = map(int, input().split())
    if (x, y) == (0, 0):
        exit()
    if x > y:
        x, y = y, x
    print(x, y)
