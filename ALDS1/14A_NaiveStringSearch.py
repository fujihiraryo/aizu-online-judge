t = input()
p = input()
m, n = len(t), len(p)
for i in range(m - n + 1):
    if t[i : i + n] == p:
        print(i)
