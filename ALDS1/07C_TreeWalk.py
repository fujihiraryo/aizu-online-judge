n = int(input())
left, right = [-1] * n, [-1] * n
parent = [-1] * n
for i in range(n):
    a, x, y = map(int, input().split())
    left[a] = x
    right[a] = y
    parent[x] = a
    parent[y] = a


def walk(root, t):
    if root == -1:
        return []
    elif t == 0:
        return [root] + walk(left[root], 0) + walk(right[root], 0)
    elif t == 1:
        return walk(left[root], 1) + [root] + walk(right[root], 1)
    else:
        return walk(left[root], 2) + walk(right[root], 2) + [root]


root = 0
for i in range(n):
    if parent[i] == -1:
        root = i
preorder = [str(i) for i in walk(root, 0)]
inorder = [str(i) for i in walk(root, 1)]
postorder = [str(i) for i in walk(root, 2)]

space = " "
print("Preorder")
print(space + space.join(preorder))
print("Inorder")
print(space + space.join(inorder))
print("Postorder")
print(space + space.join(postorder))
