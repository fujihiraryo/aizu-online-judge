n = int(input())
a, b = 0, 0
for i in range(n):
    x, y = input().split()
    if x < y:
        b += 3
    elif x > y:
        a += 3
    else:
        a += 1
        b += 1
print(a, b)
