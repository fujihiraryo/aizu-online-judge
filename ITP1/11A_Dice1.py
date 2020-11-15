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


(*x,) = map(int, input().split())
dice = Dice(x)
A = input()
for a in A:
    if a == "N":
        dice.N()
    if a == "E":
        dice.E()
    if a == "S":
        dice.S()
    if a == "W":
        dice.W()
print(dice.top)
