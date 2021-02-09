n, s = map(int, input().split())
(*a,) = map(int, input().split())
j, x = 0, 0
cnt = [0] * s
ans = n + 1
for i in range(n):
    while j < n and x < s:
        x += a[j]
        j += 1
    if x >= s:
        ans = min(ans, j - i)
    x -= a[i]
print(ans % (n + 1))
