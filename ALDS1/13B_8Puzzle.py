graph = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7],
]
start = []
for i in range(3):
    (*raw,) = map(int, input().split())
    start += raw
place = start.index(0)
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
queue = [(start, place, 0)]
visited = set()
for state, place, cnt in queue:
    visited.add(tuple(state))
    if state == goal:
        print(cnt)
        exit()
    for k in graph[place]:
        nx = state[:]
        nx[k], nx[place] = nx[place], nx[k]
        if tuple(nx) in visited:
            continue
        queue.append((nx, k, cnt + 1))
