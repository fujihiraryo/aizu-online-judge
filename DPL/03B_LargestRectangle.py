def maximum_rectangle(a):
    n = len(a)
    # left limit
    left = [None] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        left[i] = stack[-1] + 1 if stack else 0
        stack.append(i)
    # right limit
    right = [None] * n
    stack = []
    for i in range(n)[::-1]:
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        right[i] = stack[-1] - 1 if stack else n - 1
        stack.append(i)
    # maximize
    ans = 0
    for i in range(n):
        ans = max(ans, a[i] * (right[i] - left[i] + 1))
    return ans


h, w = map(int, input().split())
c = [input().split() for _ in range(h)]
ans = 0
a = [0] * w
for i in range(h):
    a = [a[j] + 1 if c[i][j] == "0" else 0 for j in range(w)]
    ans = max(ans, maximum_rectangle(a))
print(ans)
