def partition(A, a, b):
    x = A[b - 1]
    i = a - 1
    for j in range(a, b - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[b - 1] = A[b - 1], A[i + 1]
    return i + 1


n = int(input())
(*A,) = map(int, input().split())
r = str(A[-1])
partition(A, 0, n)
A = list(map(str, A))
B = []
flg = True
for a in A[::-1]:
    if a == r and flg:
        b = "[{}]".format(a)
        flg = False
    else:
        b = a
    B.append(b)
print(*B[::-1])
