while True:
    a = input()
    if a == "0":
        exit()
    a = map(int, list(a))
    print(sum(a))
