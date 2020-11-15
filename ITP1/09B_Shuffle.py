while True:
    w = input()
    if w == "-":
        exit()
    m = int(input())
    for i in range(m):
        h = int(input())
        w = w[h:] + w[:h]
    print(w)
