class RollingHash:
    def __init__(self, array, base, mod=10 ** 9 + 7):
        code = 0
        for i, x in enumerate(array):
            code += x * pow(base, i, mod)
            code %= mod
        self.code = code
        self.size = len(array)
        self.base = base
        self.mod = mod
        self.inv_base = pow(base, mod - 2, mod)

    def slide(self, x, y):
        self.code -= x
        self.code += y * pow(self.base, self.size, self.mod)
        self.code *= self.inv_base
        self.code %= self.mod


base0 = 101
base1 = 103
h, w = map(int, input().split())
field = [[ord(c) for c in input()] for _ in range(h)]
r, c = map(int, input().split())
pattern = [[ord(c) for c in input()] for _ in range(r)]
if h < r or w < c:
    exit()
# field_hash
row_hash = [[None] * (w - c + 1) for _ in range(h)]
for i in range(h):
    rh = RollingHash(field[i][0:c], base0)
    for j in range(w - c + 1):
        row_hash[i][j] = rh.code
        if j == w - c:
            break
        rh.slide(field[i][j], field[i][j + c])
field_hash = [[None] * (w - c + 1) for _ in range(h - r + 1)]
for j in range(w - c + 1):
    tmp = [row_hash[i][j] for i in range(r)]
    rh = RollingHash(tmp, base1)
    for i in range(h - r + 1):
        field_hash[i][j] = rh.code
        if i == h - r:
            break
        rh.slide(row_hash[i][j], row_hash[i + r][j])
# pattern_hash
row_hash = [None] * r
for i in range(r):
    rh = RollingHash(pattern[i], base0)
    row_hash[i] = rh.code
pattern_hash = RollingHash(row_hash, base1).code
# search
for i in range(h - r + 1):
    for j in range(w - c + 1):
        if field_hash[i][j] == pattern_hash:
            print(i, j)
