import math

a, b, C = map(int, input().split())
S = a * b * math.sin(C * math.pi / 180) / 2
L = a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(C * math.pi / 180)) ** 0.5
h = 2 * S / a
print(S)
print(L)
print(h)
