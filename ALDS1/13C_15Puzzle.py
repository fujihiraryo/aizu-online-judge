import heapq
from collections import defaultdict
from copy import deepcopy


class PriorityQuene:
    def __init__(self):
        self.heap = []
        self.count = defaultdict(int)

    def push(self, x):
        heapq.heappush(self.heap, x)
        self.count[x] += 1

    def pop(self):
        res = self.top()
        self.remove(res)
        return res

    def __bool__(self):
        return bool(self.heap)


class SlidePuzzle:
    def __init__(self, state, place=None):
        self.size = len(state)
        self.state = state
        self.place = place
        if self.place is None:
            self.place = [None] * (self.size ** 2)
            for i in range(self.size):
                for j in range(self.size):
                    self.place[self.state[i][j]] = (i, j)

    def copy(self):
        state = deepcopy(self.state)
        place = deepcopy(self.place)
        return SlidePuzzle(state, place)

    def slide(self):
        i, j = self.place[0]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= i + di < self.size and 0 <= j + dj < self.size:
                other = self.copy()
                other.state[i + di][j + dj] = self.state[i][j]
                other.state[i][j] = self.state[i + di][j + dj]
                x = other.state[i][j]
                other.place[x] = self.place[0]
                other.place[0] = self.place[x]
                yield other

    def distance(self):
        d = 0
        i, j = self.place[0]
        i0 = self.size - 1
        j0 = self.size - 1
        d += abs(i - i0) + abs(j - j0)
        for x in range(1, self.size ** 2):
            i, j = self.place[x]
            i0 = (x - 1) // self.size
            j0 = (x - 1) % self.size
            d += abs(i - i0) + abs(j - j0)
        return d

    def encode(self):
        res = 0
        for i in range(self.size):
            for j in range(self.size):
                x = self.state[i][j]
                a = self.size ** 2
                res += a ** (i * self.size + j) * x
        return res

    def __lt__(self, other):
        return True


state = [list(map(int, input().split())) for _ in range(4)]
puzzle = SlidePuzzle(state)
heap = PriorityQuene()
heap.push((puzzle.distance(), puzzle, 0))
visited = set()
loop_cnt = 0
while heap:
    loop_cnt += 1
    cost, puzzle, cnt = heap.pop()
    print(puzzle.state, cost, cnt)
    code = puzzle.encode()
    if code in visited or cost > 45:
        continue
    visited.add(code)
    dist = puzzle.distance()
    if dist == 0:
        print(cnt)
        print(loop_cnt)
        exit()
    for nx in puzzle.slide():
        heap.push((nx.distance() + cnt + 1, nx, cnt + 1))
