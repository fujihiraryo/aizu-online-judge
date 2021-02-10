n = int(input())
matrix = [[0] * n for _ in range(n)]
for _ in range(n):
    x, _, *lst = map(int, input().split())
    for y in lst:
        matrix[x - 1][y - 1] = 1
for raw in matrix:
    print(*raw)
