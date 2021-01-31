class BIT:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * (n + 1)

    def __getitem__(self, i):
        return self.sum(i + 1) - self.sum(i)

    def sum(self, i):
        s = 0
        tmp = i
        while tmp:
            s += self.arr[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        tmp = i + 1
        while tmp <= self.size:
            self.arr[tmp] += x
            tmp += tmp & -tmp


n, q = map(int, input().split())
bit = BIT(n)
for _ in range(q):
    (*query,) = map(int, input().split())
    if query[0] == 0:
        i, x = query[1], query[2]
        bit.add(i - 1, x)
    else:
        i, j = query[1], query[2]
        print(bit.sum(j) - bit.sum(i - 1))
