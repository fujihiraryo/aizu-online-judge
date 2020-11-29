def chi_liu(edges, n, r):
    A = [(INF, -1) for _ in range(n)]
    for i, j, w in edges:
        A[j] = min(A[j], (w, i))
    A[r] = (-1, -1)
    group = [0] * n
    composed = [False] * n
    cnt = 0
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        visited = []
        now = i
        while not used[now] and now != -1:
            visited.append(now)
            used[now] = True
            now = A[now][1]
        if now != -1:
            cycle = False
            for j in visited:
                group[j] = cnt
                if j == now:
                    cycle = True
                    composed[cnt] = True
                if not cycle:
                    cnt += 1
            if cycle:
                cnt += 1
        else:
            for j in visited:
                group[j] = cnt
                cnt += 1
    if cnt == n:
        return sum(map(lambda x: x[0], A)) + 1
    ret = sum(A[i][0] for i in range(n) if i != r and composed[group[i]])
    new_edges = []
    for i, j, w in edges:
        if group[i] == group[j]:
            continue
        if composed[group[j]]:
            new_edges.append((group[i], group[j], w - A[j][0]))
        else:
            new_edges.append((group[i], group[j], w))
    return ret + chi_liu(new_edges, cnt, group[r])


INF = 10 ** 18
n, m, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(chi_liu(edges, n, r))
