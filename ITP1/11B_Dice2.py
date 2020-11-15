class Dice:
    def __init__(self, x):
        self.top = x[0]
        self.front = x[1]
        self.right = x[2]
        self.left = x[3]
        self.back = x[4]
        self.bottom = x[5]

    def N(self):
        self.top, self.front, self.bottom, self.back = (
            self.front,
            self.bottom,
            self.back,
            self.top,
        )

    def E(self):
        self.top, self.right, self.bottom, self.left = (
            self.left,
            self.top,
            self.right,
            self.bottom,
        )

    def S(self):
        self.top, self.front, self.bottom, self.back = (
            self.back,
            self.top,
            self.front,
            self.bottom,
        )

    def W(self):
        self.top, self.right, self.bottom, self.left = (
            self.right,
            self.bottom,
            self.left,
            self.top,
        )

    def up_front_to_right(self, top, front):
        if (top, front) in [
            (self.top, self.front),
            (self.front, self.bottom),
            (self.bottom, self.back),
            (self.back, self.top),
        ]:
            return self.right
        if (top, front) in [
            (self.front, self.top),
            (self.bottom, self.front),
            (self.back, self.bottom),
            (self.top, self.back),
        ]:
            return self.left
        if (top, front) in [
            (self.left, self.front),
            (self.front, self.right),
            (self.right, self.back),
            (self.back, self.left),
        ]:
            return self.top
        if (top, front) in [
            (self.front, self.left),
            (self.right, self.front),
            (self.back, self.right),
            (self.left, self.back),
        ]:
            return self.bottom
        if (top, front) in [
            (self.top, self.left),
            (self.left, self.bottom),
            (self.bottom, self.right),
            (self.right, self.top),
        ]:
            return self.front
        if (top, front) in [
            (self.left, self.top),
            (self.bottom, self.left),
            (self.right, self.bottom),
            (self.top, self.right),
        ]:
            return self.back


(*x,) = map(int, input().split())
dice = Dice(x)
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    print(dice.up_front_to_right(a, b))
