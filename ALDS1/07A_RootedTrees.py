n = int(input())
parent = [-1 for i in range(n)]
children = [[] for i in range(n)]
for i in range(n):
    *ipt, = map(int, input().split())
    x = ipt[0]
    children[x] = ipt[2:]
    for c in children[x]:
        parent[c] = x
for i in range(n):
    depth = 0
    tmp = i
    while parent[tmp] != -1:
        depth += 1
        tmp = parent[tmp]
    if depth == 0:
        type = "root"
    elif children[i] != []:
        type = "internal node"
    else:
        type = "leaf"
    print(
        f"node {i}: parent = {parent[i]}, depth = {depth}, {type}, {children[i]}"
    )
