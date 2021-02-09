n, t = map(int, input().split())
time = [0] * (t + 1)
for i in range(n):
    li, ri = map(int, input().split())
    time[li] += 1
    time[ri] -= 1
for i in range(1, t + 1):
    time[i] += time[i - 1]
print(max(time))
