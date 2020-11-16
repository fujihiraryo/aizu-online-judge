from collections import defaultdict


class BinarySearchTree:
    def __init__(self):
        self.left = defaultdict(lambda: None)
        self.right = defaultdict(lambda: None)
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = x
            return
        p, y = None, self.root
        while y is not None:
            p = y
            if x < y:
                y = self.left[y]
            else:
                y = self.right[y]
        if x < p:
            self.left[p] = x
        else:
            self.right[p] = x

    def _walk(self, root, t):
        if root is None:
            return []
        elif t == 0:
            return (
                [root]
                + self._walk(self.left[root], 0)
                + self._walk(self.right[root], 0)
            )
        else:
            return (
                self._walk(self.left[root], 1)
                + [root]
                + self._walk(self.right[root], 1)
            )

    def preorder(self):
        return self._walk(self.root, 0)

    def inorder(self):
        return self._walk(self.root, 1)


n = int(input())
tree = BinarySearchTree()
for i in range(n):
    command = input().split()
    if len(command) > 1:
        x = int(command[1])
        tree.insert(x)
    else:
        print(" " + " ".join(map(str, tree.inorder())))
        print(" " + " ".join(map(str, tree.preorder())))
