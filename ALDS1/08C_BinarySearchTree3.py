class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        x = Node(key)
        if self.root is None:
            self.root = x
            return
        y = self.root
        while y is not None:
            p = y
            if x.key < y.key:
                y = y.left
            else:
                y = y.right
        x.parent = p
        if x.key < p.key:
            p.left = x
        else:
            p.right = x

    def __preorder(self, root):
        if root is None:
            return
        yield root
        for x in self.__preorder(root.left):
            yield x
        for x in self.__preorder(root.right):
            yield x

    def preorder(self):
        for x in self.__preorder(self.root):
            yield x.key

    def __inorder(self, root):
        if root is None:
            return
        for x in self.__inorder(root.left):
            yield x
        yield root
        for x in self.__inorder(root.right):
            yield x

    def inorder(self):
        for x in self.__inorder(self.root):
            yield x.key

    def __find(self, key, root):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return self.__find(key, root.left)
        else:
            return self.__find(key, root.right)

    def find(self, key):
        return self.__find(key, self.root) is not None

    def __min(self, root):
        if root.left is None:
            return root
        return self.__min(root.left)

    def __next(self, x):
        if x.right is None:
            return x.parent
        return self.__min(x.right)

    def __trans(self, x, y):
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        if y is not None:
            y.parent = x.parent

    def delete(self, key):
        x = self.__find(key, self.root)
        if x is None:
            return
        if x.left is None:
            self.__trans(x, x.right)
        elif x.right is None:
            self.__trans(x, x.left)
        else:
            y = self.__next(x)
            if x != y.parent:
                self.__trans(y, y.right)
                y.right = x.right
                y.right.parent = y
            self.__trans(x, y)
            y.left = x.left
            y.left.parent = y


tree = BinarySearchTree()
for _ in range(int(input())):
    command = input().split()
    if command[0] == "insert":
        tree.insert(int(command[1]))
    if command[0] == "find":
        print("yes" if tree.find(int(command[1])) else "no")
    if command[0] == "print":
        print(" " + " ".join(map(str, tree.inorder())))
        print(" " + " ".join(map(str, tree.preorder())))
    if command[0] == "delete":
        tree.delete(int(command[1]))
