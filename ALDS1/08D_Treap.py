class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def __insert(self, x, key, priority):
        if x is None:
            return Node(key, priority)
        if key == x.key:
            return x
        if key < x.key:
            x.left = self.__insert(x.left, key, priority)
            if x.priority < x.left.priority:
                x = self.rotate_right(x)
        else:
            x.right = self.__insert(x.right, key, priority)
            if x.priority < x.right.priority:
                x = self.rotate_left(x)
        return x

    def insert(self, key, priority):
        self.root = self.__insert(self.root, key, priority)

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

    def __delete(self, x, key):
        if x is None:
            return None
        if key < x.key:
            x.left = self.__delete(x.left, key)
        elif key > x.key:
            x.right = self.__delete(x.right, key)
        else:
            if x.left is None and x.right is None:
                return None
            elif x.left is None:
                x = self.rotate_left(x)
            elif x.right is None:
                x = self.rotate_right(x)
            else:
                if x.left.priority > x.right.priority:
                    x = self.rotate_right(x)
                else:
                    x = self.rotate_left(x)
            return self.__delete(x, key)
        return x

    def delete(self, key):
        self.root = self.__delete(self.root, key)


tree = Treap()
for _ in range(int(input())):
    command = input().split()
    if command[0] == "insert":
        tree.insert(int(command[1]), int(command[2]))
    if command[0] == "find":
        print("yes" if tree.find(int(command[1])) else "no")
    if command[0] == "print":
        print(" " + " ".join(map(str, tree.inorder())))
        print(" " + " ".join(map(str, tree.preorder())))
    if command[0] == "delete":
        tree.delete(int(command[1]))
