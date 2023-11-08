class Heap:
    def __init__(self):
        self.data = []

    def insert(self, x):
        i = len(self.data)
        self.data.append(x)
        while i > 0 and self.data[i] > self.data[(i - 1) // 2]:
            p = (i - 1) // 2
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p

    def extract(self):
        if len(self.data) == 1:
            return self.data.pop()
        x = self.data[0]
        self.data[0] = self.data.pop()
        i = 0
        n = len(self.data)
        while True:
            c1 = 2 * i + 1
            c2 = 2 * i + 2
            if c2 < n:
                if self.data[i] < self.data[c1] < self.data[c2]:
                    self.data[i], self.data[c2] = self.data[c2], self.data[i]
                    i = c2
                    continue
                if self.data[i] < self.data[c2] < self.data[c1]:
                    self.data[i], self.data[c1] = self.data[c1], self.data[i]
                    i = c1
                    continue
                if self.data[i] < self.data[c1]:
                    self.data[i], self.data[c1] = self.data[c1], self.data[i]
                    i = c1
                    continue
                if self.data[i] < self.data[c2]:
                    self.data[i], self.data[c2] = self.data[c2], self.data[i]
                    i = c2
                    continue
            elif c1 < n:
                if self.data[i] < self.data[c1]:
                    self.data[i], self.data[c1] = self.data[c1], self.data[i]
                    i = c1
                    continue
            break
        return x


h = Heap()

while True:
    s = input()
    if s == "end":
        break
    if s[0] == "i":
        _, x = s.split()
        h.insert(int(x))
    else:
        print(h.extract())
