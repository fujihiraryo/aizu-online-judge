from itertools import combinations

n = int(input())
(*A,) = map(int, input().split())
q = int(input())
(*M,) = map(int, input().split())
S = set()
for i in range(1, n + 1):
    for c in combinations(A, i):
        S.add(sum(c))
for m in M:
    if m in S:
        print("yes")
    else:
        print("no")
