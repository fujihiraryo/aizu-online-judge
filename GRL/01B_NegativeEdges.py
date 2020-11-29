INF = 10 ** 20
n, m, r = map(int, input().split())
E = [tuple(map(int, input().split())) for j in range(m)]
D = [INF for i in range(n)]
D[r] = 0
flag = True
cnt = 0
while flag:
    flag = False
    cnt += 1
    if cnt > n:
        print("NEGATIVE CYCLE")
        exit()
    for s, t, d in E:
        if D[s] != INF and D[t] > D[s] + d:
            D[t] = D[s] + d
            flag = True
for i in range(n):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])
