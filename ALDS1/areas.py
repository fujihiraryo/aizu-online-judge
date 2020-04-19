S = input()
left, right, area = [], [], []
for i, s in enumerate(list(S)):
    if s == '\\':
        left.append(i)
    if s == '/' and left != []:
        j = left.pop()
        a = i - j
        while right != [] and j < right[-1]:
            right.pop()
            a += area.pop()
        right.append(j)
        area.append(a)
print(sum(area))
print(len(area), *area)
