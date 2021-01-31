import random

x_min, x_max = -(10 ** 10), 10 ** 10
n = 5 * 10 ** 5
print(n)
for _ in range(n):
    x = random.randint(x_min, x_max)
    y = random.randint(x_min, x_max)
    print(x, y)
q = 2 * 10 ** 4
print(q)
for _ in range(q):
    sx = random.randint(-100, 100)
    tx = random.randint(-100, 100)
    sy = random.randint(-100, 100)
    ty = random.randint(-100, 100)
    if sx > tx:
        sx, tx = tx, sx
    if sy > ty:
        sy, ty = ty, sy
    print(sx, tx, sy, ty)
