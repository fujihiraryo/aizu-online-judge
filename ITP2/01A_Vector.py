a = []
for _ in range(int(input())):
    (*query,) = map(int, input().split())
    if query[0] == 0:
        a.append(query[1])
    elif query[0] == 1:
        print(a[query[1]])
    else:
        a.pop()
