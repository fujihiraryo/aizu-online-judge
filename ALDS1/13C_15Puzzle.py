import heapq

n = 4
n2 = n ** 2
limit = 45

board = [list(map(int, input().split())) for _ in range(n)]
code = 0
dist = 0
for i in range(n):
    for j in range(n):
        x = board[i][j]
        if x == 0:
            k0 = i * n + j
        else:
            ix, jx = (x - 1) // n, (x - 1) % n
            dist += abs(i - ix) + abs(j - jx)
        code += x * pow(n2, i * n + j)

heap = [(dist, dist, 0, code, k0)]
visited = set()
while heap:
    cost, dist, cnt, code, k0 = heapq.heappop(heap)
    if dist == 0:
        print(cnt)
        exit()
    if (cost > limit) or (code in visited):
        continue
    visited.add(code)
    i0, j0 = k0 // n, k0 % n
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i, j = i0 + di, j0 + dj
        if i < 0 or i >= n or j < 0 or j >= n:
            continue
        k = i * n + j
        x = (code // pow(n2, k)) % n2
        new_code = code + x * (pow(n2, k0) - pow(n2, k))
        new_dist = dist
        new_dist -= abs(i - (x - 1) // n) + abs(j - (x - 1) % n)
        new_dist += abs(i0 - (x - 1) // n) + abs(j0 - (x - 1) % n)
        new_cnt = cnt + 1
        new_cost = new_dist + new_cnt
        heapq.heappush(heap, (new_cost, new_dist, new_cnt, new_code, k))
