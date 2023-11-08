n = int(input())
ans = 0
d, n = n // 25, n % 25
ans += d
d, n = n // 10, n % 10
ans += d
d, n = n // 5, n % 5
ans += d
ans += n
print(ans)
