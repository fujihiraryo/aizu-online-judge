n, k = map(int, input().split())
(*a,) = map(int, input().split())
a = [a[i] - 1 for i in range(n)]
ans = n + 1
cnt = [0] * k
j, x = 0, 0
for i in range(n):
    while j < n and x < k:
        if a[j] < k:
            cnt[a[j]] += 1
            if cnt[a[j]] == 1:
                x += 1
        j += 1
    if x == k:
        ans = min(ans, j - i)
    if a[i] < k:
        cnt[a[i]] -= 1
        if cnt[a[i]] == 0:
            x -= 1
print(ans % (n + 1))
