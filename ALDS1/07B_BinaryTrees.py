n = int(input())
parent = [-1 for i in range(n)]
brother = [-1 for i in range(n)]
degree = [0 for i in range(n)]
depth = [0 for i in range(n)]
height = [0 for i in range(n)]

for i in range(n):
    a, x, y = map(int, input().split())
    if x != -1:
        parent[x] = a
        brother[x] = y
        degree[a] += 1
    if y != -1:
        parent[y] = a
        brother[y] = x
        degree[a] += 1

for i in range(n):
    tmp = i
    while parent[tmp] != -1:
        depth[i] += 1
        height[parent[tmp]] = max(height[parent[tmp]], depth[i])
        tmp = parent[tmp]

for i in range(n):
    if depth[i] == 0:
        type = "root"
    elif degree[i] != 0:
        type = "internal node"
    else:
        type = "leaf"
    print(
        f"node {i}: parent = {parent[i]}, sibling = {brother[i]}, degree = {degree[i]}, depth = {depth[i]}, height = {height[i]}, {type}"
    )
