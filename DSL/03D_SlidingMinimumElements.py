import heapq
from collections import defaultdict


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

    def top(self):
        return self.heap[0]

    def remove(self, x):
        if self.count[x] == 0:
            return
        self.count[x] -= 1
        while self.heap:
            if self.count[self.top()]:
                break
            heapq.heappop(self.heap)

    def __bool__(self):
        return bool(self.heap)


n, k = map(int, input().split())
(*a,) = map(int, input().split())
p = PriorityQuene()
for i in range(k):
    p.push(a[i])
ans = [p.top()]
for i in range(k, n):
    p.remove(a[i - k])
    p.push(a[i])
    ans.append(p.top())
print(*ans)
