import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = deque([])
for i in range(n):
    inp = input().split()
    op = inp[0]
    try:
        x = inp[1]
    except KeyError:
        pass
    if op == "insert":
        lst.appendleft(x)
    if op == "delete":
        try:
            lst.remove(x)
        except ValueError:
            pass
    if op == "deleteFirst":
        lst.popleft()
    if op == "deleteLast":
        lst.pop()
print(*lst)
