while True:
    a, b = map(int, input().split())
    if a * b == 0:
        exit()
    for i in range(a):
        print('#' * b)
    print()
