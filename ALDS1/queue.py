from collections import deque
n, q = map(int, input().split())
lst = deque([])
for i in range(n):
    name, time = input().split()
    lst.append({'name': name, 'time': int(time)})
now = 0
while len(lst) > 0:
    task = lst.popleft()
    now += min(q, task['time'])
    task['time'] -= q
    if task['time'] > 0:
        lst.append(task)
    else:
        print(task['name'], now)
