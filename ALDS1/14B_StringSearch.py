base = 100
mod = 10 ** 9 + 7
inv = pow(base, mod - 2, mod)
t = input()
p = input()
m, n = len(t), len(p)
if m < n:
    exit()
a, b = 0, 0
for i in range(n):
    a += ord(t[i]) * pow(base, i, mod)
    a %= mod
    b += ord(p[i]) * pow(base, i, mod)
    b %= mod
for i in range(m - n + 1):
    if a == b:
        print(i)
    if i == m - n:
        break
    a -= ord(t[i])
    a += ord(t[i + n]) * pow(base, n, mod)
    a *= inv
    a %= mod
