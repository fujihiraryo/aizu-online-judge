import math


def split3(a, b):
    s = (a[0] * (2 / 3) + b[0] * (1 / 3), a[1] * (2 / 3) + b[1] * (1 / 3))
    t = (a[0] * (1 / 3) + b[0] * (2 / 3), a[1] * (1 / 3) + b[1] * (2 / 3))
    return s, t


def rotate60(s, t):
    th = math.pi / 3
    u0 = s[0] + math.cos(th) * (t[0] - s[0]) - math.sin(th) * (t[1] - s[1])
    u1 = s[1] + math.sin(th) * (t[0] - s[0]) + math.cos(th) * (t[1] - s[1])
    return (u0, u1)


lst = [(0, 0), (100, 0)]
n = int(input())

for i in range(n):
    L = len(lst)
    new_lst = []
    for x in range(L - 1):
        left = lst[x]
        right = lst[x + 1]
        new_lst.append(left)
        s, t = split3(left, right)
        u = rotate60(s, t)
        new_lst.append(s)
        new_lst.append(u)
        new_lst.append(t)
    new_lst.append(right)
    lst = new_lst
for p in lst:
    print(*p)
