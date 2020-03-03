from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
lst = deque([])
for i in range(n):
    inp = input().split()
    op = inp[0]
    try:
        x = inp[1]
    except:
        pass
    if op == 'insert':
        lst.appendleft(x)
    if op == 'delete':
        try:
            lst.remove(x)
        except:
            pass
    if op == 'deleteFirst':
        lst.popleft()
    if op == 'deleteLast':
        lst.pop()
print(*lst)
