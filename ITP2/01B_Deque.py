from collections import deque

a = deque()
for _ in range(int(input())):
    (*query,) = map(int, input().split())
    if query[0] == 0:
        if query[1] == 0:
            a.appendleft(query[2])
        else:
            a.append(query[2])
    elif query[0] == 1:
        print(a[query[1]])
    else:
        if query[1] == 0:
            a.popleft()
        else:
            a.pop()
