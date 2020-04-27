n, m, r = map(int, input().split())
E = [tuple(map(int, input().split())) for j in range(m)]
inf = 10**20
D = [inf for i in range(n)]
D[r] = 0
flag = True
cnt = 0
while flag:
    flag = False
    cnt += 1
    if cnt > n:
        print('NEGATIVE CYCLE')
        exit()
    for s, t, d in E:
        if D[s] != inf and D[t] > D[s]+d:
            D[t] = D[s]+d
            flag = True
for i in range(n):
    if D[i] == inf:
        print('INF')
    else:
        print(D[i])
