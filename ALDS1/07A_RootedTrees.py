n = int(input())
parent = [-1 for i in range(n)]
children = [[] for i in range(n)]
for i in range(n):
    (*ipt,) = map(int, input().split())
    x = ipt[0]
    children[x] = ipt[2:]
    for c in children[x]:
        parent[c] = x
for i in range(n):
    d = 0
    tmp = i
    while parent[tmp] != -1:
        d += 1
        tmp = parent[tmp]
    if d == 0:
        t = "root"
    elif children[i] != []:
        t = "internal node"
    else:
        t = "leaf"
    p = parent[i]
    c = children[i]
    print(f"node {i}: parent = {p}, depth = {d}, {t}, {c}")
