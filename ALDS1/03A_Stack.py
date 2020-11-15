def ope(a, x, y):
    if a == "+":
        return x + y
    if a == "-":
        return x - y
    if a == "*":
        return x * y


(*A,) = input().split()
stack = []
for a in A:
    try:
        a = int(a)
        stack.append(a)
    except:
        tmp = stack.pop()
        tmp = ope(a, stack.pop(), tmp)
        stack.append(tmp)
print(stack.pop())
