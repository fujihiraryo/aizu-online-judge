from itertools import permutations


def check(x):
    for i in range(7):
        for j in range(i + 1, 8):
            if abs(i - j) == abs(x[i] - x[j]):
                return False
    return True


n = int(input())
lst = []
for _ in range(n):
    r, c = map(int, input().split())
    lst.append((r, c))
for x in permutations(range(8)):
    if all(x[r] == c for r, c in lst) and check(x):
        break
for i in range(8):
    raw = ["."] * 8
    raw[x[i]] = "Q"
    print("".join(raw))
