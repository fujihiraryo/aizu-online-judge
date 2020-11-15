N = int(input())
(*A,) = map(int, input().split())
ok = False
count = 0
while not ok:
    ok = True
    for i in range(N - 1):
        j = N - 1 - i
        if A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            count += 1
            ok = False
print(*A)
print(count)
