N = int(input())
* A, = map(int, input().split())
count = 0
for i in range(N):
    minj = i
    for j in range(i+1, N):
        if A[j] < A[minj]:
            minj = j
    A[i], A[minj] = A[minj], A[i]
    if i != minj:
        count += 1
print(*A)
print(count)
