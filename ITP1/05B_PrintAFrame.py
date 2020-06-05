while True:
    a, b = map(int, input().split())
    if a * b == 0:
        exit()
    for i in range(a):
        if i == 0 or i == a - 1:
            print("#" * b)
        else:
            print("#" + "." * (b - 2) + "#")
    print()
