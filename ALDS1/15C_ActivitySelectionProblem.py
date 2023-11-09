n = int(input())
lst = []
for _ in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))
lst.sort(key=lambda x: x[1])
ans = 0
now = 0
for s, t in lst:
    if now <= s:
        ans += 1
        now = t + 1
print(ans)
