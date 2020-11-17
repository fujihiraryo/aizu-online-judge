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

    def preorder(self, root=-1):
        if root == -1:
            root = self.root
        if root is None:
            return
        yield root
        for x in self.preorder(self.left[root]):
            yield x
        for x in self.preorder(self.right[root]):
            yield x

    def inorder(self, root=-1):
        if root == -1:
            root = self.root
        if root is None:
            return
        for x in self.inorder(self.left[root]):
            yield x
        yield root
        for x in self.inorder(self.right[root]):
            yield x

    def find(self, x, root=-1):
        if root == -1:
            root = self.root
        if root == x:
            return True
        if root is None:
            return False
        if x < root:
            return self.find(x, root=self.left[root])
        if root < x:
            return self.find(x, root=self.right[root])


tree = BinarySearchTree()
for _ in range(int(input())):
    command = input().split()
    if command[0] == "insert":
        x = int(command[1])
        tree.insert(x)
    if command[0] == "find":
        x = int(command[1])
        print("yes" if tree.find(x) else "no")
    if command[0] == "print":
        print(" " + " ".join(map(str, tree.inorder())))
        print(" " + " ".join(map(str, tree.preorder())))
